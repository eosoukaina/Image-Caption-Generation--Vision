"""
Image Caption Generator Web Application

A production-ready Flask application that generates descriptive captions
for uploaded images using deep learning (CNN + LSTM).
"""

import os
import logging
from pathlib import Path
from typing import Optional, Tuple
import pickle

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.models import load_model

from config import get_config


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ImageCaptionModel:
    """Wrapper class for image caption generation model"""
    
    def __init__(self, model_path: Path, tokenizer_path: Path, max_length: int = 32):
        """
        Initialize the caption generation model
        
        Args:
            model_path: Path to the trained model file
            tokenizer_path: Path to the tokenizer pickle file
            max_length: Maximum length of generated captions
        """
        self.max_length = max_length
        self.model = None
        self.tokenizer = None
        self.feature_extractor = None
        
        try:
            logger.info("Loading caption generation model...")
            self.model = load_model(str(model_path))
            
            logger.info("Loading tokenizer...")
            with open(tokenizer_path, 'rb') as f:
                self.tokenizer = pickle.load(f)
            
            logger.info("Loading Xception feature extractor...")
            self.feature_extractor = Xception(include_top=False, pooling="avg")
            
            logger.info("Model initialization completed successfully")
        except Exception as e:
            logger.error(f"Error loading models: {e}")
            raise
    
    def extract_features(self, image_path: Path) -> np.ndarray:
        """
        Extract features from an image using Xception model
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Feature vector as numpy array
            
        Raises:
            ValueError: If image cannot be processed
        """
        try:
            # Load and preprocess image
            image = Image.open(image_path)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize to expected dimensions
            image = image.resize((299, 299))
            image_array = np.array(image)
            
            # Normalize pixel values
            image_array = np.expand_dims(image_array, axis=0)
            image_array = image_array / 127.5
            image_array = image_array - 1.0
            
            # Extract features
            features = self.feature_extractor.predict(image_array, verbose=0)
            
            logger.debug(f"Features extracted successfully for {image_path}")
            return features
            
        except Exception as e:
            logger.error(f"Error extracting features from {image_path}: {e}")
            raise ValueError(f"Could not process image: {e}")
    
    def _word_for_id(self, integer: int) -> Optional[str]:
        """Convert integer back to word using tokenizer"""
        for word, index in self.tokenizer.word_index.items():
            if index == integer:
                return word
        return None
    
    def generate_caption(self, image_path: Path) -> str:
        """
        Generate a caption for an image
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Generated caption as string
        """
        try:
            # Extract image features
            photo_features = self.extract_features(image_path)
            
            # Generate caption word by word
            caption = 'start'
            for _ in range(self.max_length):
                # Encode current caption
                sequence = self.tokenizer.texts_to_sequences([caption])[0]
                sequence = pad_sequences([sequence], maxlen=self.max_length)
                
                # Predict next word
                prediction = self.model.predict([photo_features, sequence], verbose=0)
                predicted_id = np.argmax(prediction)
                
                # Convert ID to word
                word = self._word_for_id(predicted_id)
                
                if word is None or word == 'end':
                    break
                
                caption += ' ' + word
            
            # Remove start/end tokens and clean caption
            caption = caption.replace('start', '').replace('end', '').strip()
            
            logger.info(f"Caption generated: {caption}")
            return caption
            
        except Exception as e:
            logger.error(f"Error generating caption: {e}")
            raise


def create_app(config_name: str = 'default') -> Flask:
    """
    Application factory pattern
    
    Args:
        config_name: Configuration environment name
        
    Returns:
        Configured Flask application
    """
    app = Flask(__name__)
    
    # Load configuration
    config_obj = get_config(config_name)
    app.config.from_object(config_obj)
    
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Initialize model
    try:
        caption_model = ImageCaptionModel(
            model_path=app.config['MODEL_PATH'],
            tokenizer_path=app.config['TOKENIZER_PATH'],
            max_length=app.config['MAX_CAPTION_LENGTH']
        )
    except Exception as e:
        logger.error(f"Failed to initialize model: {e}")
        raise
    
    def allowed_file(filename: str) -> bool:
        """Check if file extension is allowed"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
    
    @app.route('/', methods=['GET'])
    def index():
        """Render the main upload page"""
        return render_template('index.html')
    
    @app.route('/upload', methods=['POST'])
    def upload_image():
        """Handle image upload and caption generation"""
        try:
            # Validate file presence
            if 'file' not in request.files:
                flash('No file provided', 'error')
                return redirect(url_for('index'))
            
            file = request.files['file']
            
            # Validate filename
            if file.filename == '':
                flash('No file selected', 'error')
                return redirect(url_for('index'))
            
            # Validate file type
            if not allowed_file(file.filename):
                flash('Invalid file type. Allowed types: png, jpg, jpeg, gif, webp', 'error')
                return redirect(url_for('index'))
            
            # Save file securely
            filename = secure_filename(file.filename)
            filepath = Path(app.config['UPLOAD_FOLDER']) / filename
            file.save(str(filepath))
            
            logger.info(f"File uploaded: {filename}")
            
            # Generate caption
            caption = caption_model.generate_caption(filepath)
            
            return render_template(
                'uploaded.html',
                filename=filename,
                description=caption
            )
            
        except RequestEntityTooLarge:
            flash('File too large. Maximum size is 16MB', 'error')
            return redirect(url_for('index'))
        except Exception as e:
            logger.error(f"Error processing upload: {e}")
            flash('An error occurred while processing your image', 'error')
            return redirect(url_for('index'))
    
    @app.route('/api/caption', methods=['POST'])
    def api_caption():
        """API endpoint for caption generation"""
        try:
            if 'file' not in request.files:
                return jsonify({'error': 'No file provided'}), 400
            
            file = request.files['file']
            
            if file.filename == '' or not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file'}), 400
            
            # Save and process
            filename = secure_filename(file.filename)
            filepath = Path(app.config['UPLOAD_FOLDER']) / filename
            file.save(str(filepath))
            
            # Generate caption
            caption = caption_model.generate_caption(filepath)
            
            return jsonify({
                'success': True,
                'filename': filename,
                'caption': caption
            })
            
        except Exception as e:
            logger.error(f"API error: {e}")
            return jsonify({'error': str(e)}), 500
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint for monitoring"""
        return jsonify({
            'status': 'healthy',
            'model_loaded': caption_model.model is not None
        })
    
    @app.errorhandler(404)
    def not_found(e):
        """404 error handler"""
        return render_template('index.html'), 404
    
    @app.errorhandler(500)
    def server_error(e):
        """500 error handler"""
        logger.error(f"Server error: {e}")
        return render_template('index.html'), 500
    
    return app


if __name__ == '__main__':
    # Run development server
    app = create_app('development')
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
