"""
Unit tests for Image Caption Generator
"""

import pytest
import os
from pathlib import Path
from PIL import Image
import numpy as np

# Import app components
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, ImageCaptionModel
from config import get_config


@pytest.fixture
def app():
    """Create and configure a test Flask app"""
    app = create_app('development')
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = 'tests/test_uploads'
    
    # Create test upload directory
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    yield app
    
    # Cleanup
    import shutil
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])


@pytest.fixture
def client(app):
    """Create a test client for the app"""
    return app.test_client()


@pytest.fixture
def test_image():
    """Create a test image"""
    img_path = Path('tests/test_image.jpg')
    
    # Create a simple test image
    img = Image.new('RGB', (299, 299), color='red')
    img.save(img_path)
    
    yield img_path
    
    # Cleanup
    if img_path.exists():
        img_path.unlink()


class TestRoutes:
    """Test Flask routes"""
    
    def test_index_page(self, client):
        """Test the index page loads"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Image Caption Generator' in response.data
    
    def test_health_check(self, client):
        """Test the health check endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert 'status' in data
        assert data['status'] == 'healthy'
    
    def test_upload_no_file(self, client):
        """Test upload without file"""
        response = client.post('/upload', data={})
        assert response.status_code == 302  # Redirect
    
    def test_upload_with_file(self, client, test_image):
        """Test upload with valid file"""
        with open(test_image, 'rb') as f:
            data = {'file': (f, 'test.jpg')}
            response = client.post('/upload', 
                                   data=data,
                                   content_type='multipart/form-data')
            # Should redirect or return 200
            assert response.status_code in [200, 302]


class TestConfiguration:
    """Test configuration management"""
    
    def test_development_config(self):
        """Test development configuration"""
        config = get_config('development')
        assert config.DEBUG == True
        assert config.LOG_LEVEL == 'DEBUG'
    
    def test_production_config(self):
        """Test production configuration"""
        config = get_config('production')
        assert config.DEBUG == False
        assert config.LOG_LEVEL == 'WARNING'


class TestImageProcessing:
    """Test image processing functions"""
    
    def test_allowed_file_extensions(self, app):
        """Test file extension validation"""
        with app.app_context():
            from app import allowed_file
            
            # Valid extensions
            assert allowed_file('test.jpg') == True
            assert allowed_file('test.png') == True
            assert allowed_file('test.jpeg') == True
            assert allowed_file('test.gif') == True
            
            # Invalid extensions
            assert allowed_file('test.txt') == False
            assert allowed_file('test.pdf') == False
            assert allowed_file('test') == False


# Run tests
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
