# API Documentation

## Overview

The Image Caption Generator provides both a web interface and RESTful API endpoints for programmatic access.

## Base URL

```
http://localhost:8080
```

## Endpoints

### 1. Health Check

Check if the service is running and models are loaded.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

**Status Codes:**
- `200 OK` - Service is healthy

---

### 2. Generate Caption (API)

Upload an image and receive a generated caption.

**Endpoint:** `POST /api/caption`

**Content-Type:** `multipart/form-data`

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| file | File | Yes | Image file (JPG, PNG, GIF, WEBP) |

**Request Example (curl):**
```bash
curl -X POST http://localhost:8080/api/caption \
  -F "file=@/path/to/image.jpg"
```

**Success Response:**
```json
{
  "success": true,
  "filename": "image.jpg",
  "caption": "a dog running in the grass"
}
```

**Error Response:**
```json
{
  "error": "Invalid file format"
}
```

**Status Codes:**
- `200 OK` - Caption generated successfully
- `400 Bad Request` - Invalid input (missing file, wrong format)
- `500 Internal Server Error` - Server error during processing

---

### 3. Upload via Web Interface

Upload an image through the web form.

**Endpoint:** `POST /upload`

**Content-Type:** `multipart/form-data`

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| file | File | Yes | Image file (JPG, PNG, GIF, WEBP) |

**Response:** HTML page with generated caption

**Status Codes:**
- `200 OK` - Redirects to result page
- `400 Bad Request` - Invalid input
- `413 Request Entity Too Large` - File size exceeds 16MB

---

## Error Handling

All API endpoints return appropriate HTTP status codes and error messages:

```json
{
  "error": "Error description",
  "code": "ERROR_CODE"
}
```

Common error codes:
- `NO_FILE_PROVIDED` - No file in request
- `INVALID_FILE_TYPE` - Unsupported file format
- `FILE_TOO_LARGE` - File exceeds maximum size
- `PROCESSING_ERROR` - Error during caption generation

---

## Rate Limiting

Currently, there are no rate limits. For production use, consider implementing rate limiting based on your requirements.

---

## Authentication

Currently, the API does not require authentication. For production deployments, consider adding:
- API keys
- OAuth 2.0
- JWT tokens

---

## Examples

### Python

```python
import requests

# Simple upload
url = "http://localhost:8080/api/caption"
files = {"file": open("image.jpg", "rb")}
response = requests.post(url, files=files)

if response.ok:
    data = response.json()
    print(f"Caption: {data['caption']}")
else:
    print(f"Error: {response.json()['error']}")
```

### JavaScript (Node.js)

```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

const form = new FormData();
form.append('file', fs.createReadStream('image.jpg'));

axios.post('http://localhost:8080/api/caption', form, {
  headers: form.getHeaders()
})
.then(response => {
  console.log('Caption:', response.data.caption);
})
.catch(error => {
  console.error('Error:', error.response.data);
});
```

### cURL

```bash
# Basic upload
curl -X POST http://localhost:8080/api/caption \
  -F "file=@image.jpg"

# With verbose output
curl -v -X POST http://localhost:8080/api/caption \
  -F "file=@image.jpg"

# Save response to file
curl -X POST http://localhost:8080/api/caption \
  -F "file=@image.jpg" \
  -o response.json
```

---

## Supported Image Formats

- JPEG/JPG (`.jpg`, `.jpeg`)
- PNG (`.png`)
- GIF (`.gif`)
- WebP (`.webp`)

**Maximum file size:** 16MB

---

## Response Times

Average response times:
- Feature extraction: ~1.5 seconds
- Caption generation: ~0.5 seconds
- **Total average:** 2-3 seconds per image

Response times may vary based on:
- Image size and complexity
- Server hardware (CPU/GPU)
- Concurrent requests

---

## Best Practices

1. **Resize large images** before uploading to reduce processing time
2. **Use appropriate image formats** (JPEG for photos, PNG for graphics)
3. **Implement retry logic** for network failures
4. **Cache results** when processing the same image multiple times
5. **Validate file types** on client side before uploading

---

## Troubleshooting

### Common Issues

**Issue:** "No file provided" error  
**Solution:** Ensure the form field name is `file` and the file is properly attached

**Issue:** Slow response times  
**Solution:** Check image size, consider using GPU acceleration, or resize images

**Issue:** "Invalid file type" error  
**Solution:** Verify the file extension is in the supported formats list

**Issue:** Server error (500)  
**Solution:** Check server logs in `logs/app.log` for detailed error information

---

## Support

For issues or questions:
- Open an issue on GitHub
- Email: elhadifi.soukaina@gmail.com
- Check the [FAQ](../README.md#faq)
