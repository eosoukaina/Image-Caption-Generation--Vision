# 🖼️ Image Caption Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-orange.svg)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **AI-powered image caption generation system** that automatically generates descriptive captions for images using deep learning. Built with CNN (Xception) for image feature extraction and LSTM for natural language generation.

<img width="700" height="439" alt="Image" src="https://github.com/user-attachments/assets/db2b12d5-5a95-40e5-a132-06aa499e31b5" />

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Model Details](#-model-details)
- [Deployment](#-deployment)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

The **Image Caption Generator** is a production-ready deep learning application that combines computer vision and natural language processing to automatically generate human-like descriptions for images. This project demonstrates modern data engineering practices and MLOps workflows suitable for portfolio presentation.

### What Makes This Project Professional?

✅ **Production-Ready Code**: Type hints, logging, error handling, and configuration management  
✅ **Modern Architecture**: Application factory pattern, modular design, separation of concerns  
✅ **Containerization**: Docker & Docker Compose support for easy deployment  
✅ **API Endpoints**: RESTful API with JSON responses for integration  
✅ **Professional UI**: Modern, responsive web interface with real-time feedback  
✅ **Documentation**: Comprehensive docs, code comments, and usage examples  
✅ **Best Practices**: Follows PEP 8, includes tests structure, and CI/CD ready

---

## ✨ Key Features

### 🧠 **Deep Learning Capabilities**
- **CNN Feature Extraction**: Uses pre-trained Xception model on ImageNet
- **LSTM Caption Generation**: Sequence-to-sequence model for natural language
- **Attention Mechanism**: Focuses on relevant image regions while generating text
- **Vocabulary**: 8,000+ words learned from Flickr8K dataset

### 🚀 **Application Features**
- **Web Interface**: Clean, intuitive drag-and-drop upload
- **REST API**: Programmatic access for integration
- **Batch Processing**: Support for multiple images
- **Real-time Processing**: Fast inference with optimized models
- **Health Monitoring**: Health check endpoints for deployment

### 🛠️ **Engineering Features**
- Structured logging with rotation
- Environment-based configuration
- Error handling and validation
- Docker containerization
- Gunicorn WSGI server
- Production/development modes

---

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Upload    │─────▶│   Xception   │─────▶│   Feature   │
│   Image     │      │   CNN Model  │      │   Vector    │
└─────────────┘      └──────────────┘      └─────────────┘
                                                   │
                                                   ▼
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│  Generated  │◀─────│  LSTM Decoder│◀─────│  Tokenizer  │
│   Caption   │      │    Network   │      │   + Vocab   │
└─────────────┘      └──────────────┘      └─────────────┘
```
### detailed System Architecture

<img width="611" height="344" alt="Image" src="https://github.com/user-attachments/assets/45627527-60f5-4eda-a57d-17298fb16f2e" />

### Model Pipeline

1. **Image Preprocessing**: Resize to 299×299, normalize pixel values
2. **Feature Extraction**: Xception CNN extracts 2048-dim feature vector
3. **Sequence Generation**: LSTM generates caption word-by-word
4. **Post-processing**: Remove start/end tokens, format output

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** - Programming language
- **TensorFlow 2.13** - Deep learning framework
- **Keras 2.13** - High-level neural networks API
- **Flask 2.3** - Web application framework

### Deep Learning Models
- **Xception** - Pre-trained CNN for image feature extraction
- **LSTM** - Recurrent neural network for text generation
- **Custom Architecture** - Merged model for caption generation

### DevOps & Tools
- **Docker** - Containerization
- **Gunicorn** - Production WSGI server
- **Pillow** - Image processing
- **NumPy** - Numerical operations

### Dataset
- **Flickr8K** - 8,091 images with 5 captions each (40,455 total captions)

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 4GB+ RAM (for model inference)
- (Optional) Docker & Docker Compose

### Option 1: Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/eosoukaina/image-caption-generator.git
cd image-caption-generator
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configurations
```

5. **Run the application**
```bash
python app.py
```

The application will be available at `http://localhost:8080`

### Option 2: Docker Installation

1. **Clone the repository**
```bash
git clone https://github.com/eosoukaina/image-caption-generator.git
cd image-caption-generator
```

2. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8080`

---

## 🚀 Usage

### Web Interface

1. Navigate to `http://localhost:8080`
2. Click "Choose File" or drag and drop an image
3. Click "Generate Caption"
4. View the AI-generated caption

### API Usage

#### Health Check
```bash
curl http://localhost:8080/health
```

Response:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

#### Generate Caption (API)
```bash
curl -X POST http://localhost:8080/api/caption \
  -F "file=@/path/to/image.jpg"
```

Response:
```json
{
  "success": true,
  "filename": "image.jpg",
  "caption": "a dog running in the grass"
}
```

---

## Demo 

<img width="604" height="433" alt="Image" src="https://github.com/user-attachments/assets/39d19138-1a94-47cd-b8bd-bafd710336a5" />

## 📂 Project Structure

```
image-caption-generator/
├── app.py                  # Main Flask application
├── config.py              # Configuration management
├── wsgi.py                # Production WSGI entry point
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker container definition
├── docker-compose.yml    # Docker Compose orchestration
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── LICENSE              # MIT License
│
├── models/              # Trained model files
│   └── model_9.h5      # Caption generation model
│
├── static/              # Static assets
│   ├── styles.css      # Application stylesheet
│   └── uploads/        # Uploaded images directory
│
├── templates/           # HTML templates
│   ├── index.html      # Upload page
│   └── uploaded.html   # Results page
│
├── logs/               # Application logs
│   └── app.log
│
├── tests/              # Unit and integration tests
│   └── test_app.py
│
└── docs/               # Additional documentation
    └── API.md
```

---

## 🧪 Model Details

### Training Configuration

- **Dataset**: Flickr8K (8,091 images, 40,455 captions)
- **Architecture**: CNN-LSTM Encoder-Decoder
- **CNN**: Xception (ImageNet pre-trained)
- **LSTM**: 256 units with dropout
- **Embedding**: 200-dimensional word embeddings
- **Vocabulary Size**: ~8,500 unique words
- **Max Caption Length**: 32 words

### Model Performance

| Metric | Score |
|--------|-------|
| BLEU-1 | 0.59  |
| BLEU-2 | 0.37  |
| BLEU-3 | 0.25  |
| BLEU-4 | 0.16  |

**BLEU Score** (Bilingual Evaluation Understudy):
- Score near **1.0** = Perfect match with human captions
- Score near **0.0** = Poor match with human captions

### Training Process

```python
# Simplified training pipeline
1. Load Flickr8K images and captions
2. Extract features using Xception CNN
3. Prepare sequences for LSTM training
4. Train encoder-decoder model
5. Evaluate using BLEU metrics
6. Save best model checkpoint
```

---

## 📊 Performance

### Inference Speed
- **Average**: 2-3 seconds per image
- **Feature Extraction**: ~1.5 seconds
- **Caption Generation**: ~0.5 seconds

### System Requirements
- **Minimum RAM**: 4GB
- **Recommended RAM**: 8GB+
- **Disk Space**: 500MB (for models)
- **CPU**: Multi-core recommended
- **GPU**: Optional (significant speedup)

---

## 🌐 Deployment

### Production Deployment

#### Using Gunicorn (Recommended)
```bash
gunicorn --bind 0.0.0.0:8080 --workers 2 --timeout 120 wsgi:app
```

#### Using Docker
```bash
docker build -t image-caption-generator .
docker run -p 8080:8080 image-caption-generator
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment mode | `development` |
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Flask secret key | Random |
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `8080` |
| `LOG_LEVEL` | Logging level | `INFO` |

### Cloud Deployment Options

- **Heroku**: Use included `Dockerfile`
- **AWS EC2**: Deploy with Docker or directly
- **Google Cloud Run**: Containerized deployment
- **Azure App Service**: Web app deployment

---
## Getting Started  

### Prerequisites  
Make sure you have the following installed:  
- Python 3.8+  
- TensorFlow & Keras  

### Clone the Repository  
```sh
git clone <repository-url>
cd <project-directory>
```
## Run the App
```sh
python app.py
```

---
## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Code Style

This project follows:
- **PEP 8** Python style guide
- **Type hints** for function signatures
- **Docstrings** for all functions/classes
- **Black** for code formatting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## 🙏 Acknowledgments

- **Flickr8K Dataset** - Training data
- **Keras Team** - Deep learning framework
- **TensorFlow Team** - ML infrastructure
- **Open Source Community** - Various libraries and tools

---

## 📧 Contact

For questions or suggestions, feel free to reach out :

- 📧 Email: elhadifi.soukaina@gmail.com
- 💼 LinkedIn: [Soukaina El Hadifi](https://linkedin.com/in/soukaina-el-hadifi)
- 🐙 GitHub: [@eosoukaina](https://github.com/eosoukaina)

---
</div>

**⭐ Star this repository if you find it helpful!**

</div>  


