# Deployment Guide

## Table of Contents
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [Docker Deployment](#docker-deployment)
- [Cloud Platforms](#cloud-platforms)
- [Configuration](#configuration)
- [Monitoring](#monitoring)

---

## Local Development

### Quick Start

1. **Clone and setup:**
```bash
git clone https://github.com/yourusername/image-caption-generator.git
cd image-caption-generator
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run development server:**
```bash
python app.py
```

Access at: `http://localhost:8080`

---

## Production Deployment

### Using Gunicorn (Recommended)

1. **Install Gunicorn:**
```bash
pip install gunicorn
```

2. **Run with Gunicorn:**
```bash
gunicorn --bind 0.0.0.0:8080 \
         --workers 2 \
         --timeout 120 \
         --access-logfile logs/access.log \
         --error-logfile logs/error.log \
         wsgi:app
```

### Configuration Options

**Workers:** Number of worker processes
```bash
--workers=$(( 2 * $(nproc) + 1 ))  # Recommended: (2 x CPU cores) + 1
```

**Timeout:** Request timeout in seconds
```bash
--timeout 120  # Recommended for ML inference
```

**Keep-alive:** Keep-alive connections
```bash
--keep-alive 5
```

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t image-caption-generator .
```

### Run Container

```bash
docker run -d \
  --name caption-generator \
  -p 8080:8080 \
  -v $(pwd)/static/uploads:/app/static/uploads \
  -v $(pwd)/logs:/app/logs \
  -e FLASK_ENV=production \
  image-caption-generator
```

### Using Docker Compose

```bash
docker-compose up -d
```

Stop services:
```bash
docker-compose down
```

View logs:
```bash
docker-compose logs -f
```

---

## Cloud Platforms

### Heroku

1. **Install Heroku CLI**
2. **Login:**
```bash
heroku login
```

3. **Create app:**
```bash
heroku create your-app-name
```

4. **Deploy:**
```bash
git push heroku main
```

5. **Scale:**
```bash
heroku ps:scale web=1
```

**Procfile:**
```
web: gunicorn --bind 0.0.0.0:$PORT wsgi:app
```

### AWS EC2

1. **Launch EC2 instance** (Ubuntu 20.04 LTS)
2. **SSH into instance:**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Install dependencies:**
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

4. **Clone and setup:**
```bash
git clone your-repo
cd image-caption-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. **Configure Nginx:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/app/static;
    }
}
```

6. **Create systemd service:**
```ini
[Unit]
Description=Image Caption Generator
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/app
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn --workers 2 --bind 127.0.0.1:8080 wsgi:app

[Install]
WantedBy=multi-user.target
```

### Google Cloud Run

1. **Build and push to Container Registry:**
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/caption-generator
```

2. **Deploy to Cloud Run:**
```bash
gcloud run deploy caption-generator \
  --image gcr.io/PROJECT_ID/caption-generator \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Azure App Service

1. **Login to Azure:**
```bash
az login
```

2. **Create resource group:**
```bash
az group create --name CaptionGeneratorRG --location eastus
```

3. **Create App Service plan:**
```bash
az appservice plan create --name CaptionPlan --resource-group CaptionGeneratorRG --sku B1 --is-linux
```

4. **Create web app:**
```bash
az webapp create --resource-group CaptionGeneratorRG --plan CaptionPlan --name your-app-name --runtime "PYTHON|3.9"
```

5. **Deploy:**
```bash
az webapp up --name your-app-name --resource-group CaptionGeneratorRG
```

---

## Configuration

### Environment Variables

Create `.env` file:
```bash
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8080
LOG_LEVEL=WARNING
```

Load in production:
```bash
export $(cat .env | xargs)
```

### Security Checklist

- [ ] Set strong `SECRET_KEY`
- [ ] Disable `DEBUG` mode
- [ ] Use HTTPS/SSL certificates
- [ ] Implement rate limiting
- [ ] Set up CORS policies
- [ ] Enable firewall rules
- [ ] Regular security updates
- [ ] Implement authentication (if needed)

---

## Monitoring

### Logging

Application logs are in `logs/app.log`

View real-time logs:
```bash
tail -f logs/app.log
```

### Health Checks

Monitor endpoint:
```bash
curl http://your-domain/health
```

Expected response:
```json
{"status": "healthy", "model_loaded": true}
```

### Performance Monitoring

Install monitoring tools:
```bash
pip install prometheus-client
```

Metrics to monitor:
- Request latency
- Error rates
- Memory usage
- CPU usage
- Disk space

### Automated Monitoring

**Using Uptime Robot:**
- Monitor `/health` endpoint
- Get alerts on downtime
- Free tier available

**Using New Relic:**
```bash
pip install newrelic
newrelic-admin run-program gunicorn wsgi:app
```

---

## Scaling

### Vertical Scaling
- Increase CPU/RAM
- Use GPU for faster inference
- Optimize model size

### Horizontal Scaling
- Load balancer (Nginx, HAProxy)
- Multiple application instances
- Shared storage for uploads

### Caching
- Redis for session storage
- Cache generated captions
- CDN for static files

---

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
lsof -i :8080
kill -9 <PID>
```

**Permission denied:**
```bash
chmod +x wsgi.py
sudo chown -R $USER:$USER logs/ static/uploads/
```

**Out of memory:**
- Reduce worker processes
- Implement request queuing
- Use smaller batch sizes

**Slow inference:**
- Use GPU acceleration
- Optimize image preprocessing
- Implement caching

---

## Backup and Recovery

### Backup Strategy

1. **Model files:** Store in cloud storage (S3, GCS)
2. **Uploaded images:** Regular backups
3. **Logs:** Rotate and archive
4. **Configuration:** Version control

### Database Backups (if applicable)

```bash
# Automated daily backup
0 2 * * * /path/to/backup-script.sh
```

---

## Support

For deployment issues:
- Check logs in `logs/app.log`
- Review [GitHub Issues](https://github.com/yourusername/repo/issues)
- Contact: elhadifi.soukaina@gmail.com
