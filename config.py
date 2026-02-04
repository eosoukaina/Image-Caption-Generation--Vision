"""
Configuration module for Image Caption Generator
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

class Config:
    """Base configuration"""
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Uploads
    UPLOAD_FOLDER = BASE_DIR / 'static' / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Model Configuration
    MODEL_PATH = BASE_DIR / 'models' / 'model_9.h5'
    TOKENIZER_PATH = BASE_DIR / 'tokenizer.p'
    MAX_CAPTION_LENGTH = 32
    
    # Image Processing
    IMAGE_SIZE = (299, 299)
    
    # Server
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 8080))
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = BASE_DIR / 'logs' / 'app.log'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = 'WARNING'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config(env='default'):
    """Get configuration based on environment"""
    return config.get(env, config['default'])
