#!/bin/bash

# ☁️ Cloud-Based Image Processing Service

The **Cloud-Based Image Processing Service** provides a scalable and efficient platform for uploading, processing, and downloading images via a RESTful API. It leverages real-time cloud execution and Google Cloud Storage to deliver seamless, on-demand image operations including grayscale conversion, resizing, format transformation, and watermark application (extendable).

Designed with modularity and simplicity in mind, it is well-suited for:
- 🛒 **E-commerce** (e.g., product image optimization)
- 📱 **Social media platforms** (e.g., auto-formatting and watermarking)
- 🏥 **Medical imaging** (e.g., secure cloud storage and batch processing)

---

## 📂 Project Structure

\`\`\`
cloud-image-processing/
│
├── app.py                  # Flask app logic and API routes
├── image_processor.py      # Image processing and cloud upload logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build configuration
└── processed_images/       # Directory where processed images are temporarily stored
\`\`\`

---

## 🚀 Features

- ✅ Upload image via API
- 🎨 Convert image to grayscale (can be extended to support resizing, watermarking, etc.)
- ☁️ Upload processed image to **Google Cloud Storage**
- 🔗 Get a public URL to access the processed image
- 📥 Download processed images via API
- ⚙️ Easily deployable via **Docker**
- 📈 Designed for scalability using **Cloud Run / Cloud Functions**

---

## 📦 Requirements

- Python 3.9+
- Google Cloud Account (with a Storage bucket created)
- Google Cloud credentials (\`GOOGLE_APPLICATION_CREDENTIALS\` env variable)
- Docker (for container deployment)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/your-username/cloud-image-processing.git
cd cloud-image-processing
\`\`\`

### 2. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Set environment variables

\`\`\`bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
export BUCKET_NAME="your-gcs-bucket-name"
\`\`\`

### 4. Run the Flask app locally

\`\`\`bash
python app.py
\`\`\`

---

## 🧪 API Usage

### 🔼 Upload an Image
**Endpoint:** \`POST /upload\`

**Form-data:**
- \`image\`: (binary file)

**Response:**
\`\`\`json
{
  "message": "Image processed successfully",
  "processed_image_url": "https://storage.googleapis.com/your-bucket-name/processed/example_processed.jpg"
}
\`\`\`

---

### 🔽 Download an Image
**Endpoint:** \`GET /download?filename=example_processed.jpg\`

**Response:** Returns the image as an attachment.

---

## 🐳 Docker Deployment

### 1. Create a \`requirements.txt\`

\`\`\`
Flask
Pillow
google-cloud-storage
\`\`\`

### 2. Dockerfile

\`\`\`dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8080

CMD ["python", "app.py"]
\`\`\`

### 3. Build the Docker image

\`\`\`bash
docker build -t cloud-image-service .
\`\`\`

### 4. Run the container

\`\`\`bash
docker run -p 8080:8080 \\
  -e BUCKET_NAME="your-gcs-bucket-name" \\
  -e GOOGLE_APPLICATION_CREDENTIALS="/app/key.json" \\
  -v \$(pwd)/key.json:/app/key.json \\
  cloud-image-service
\`\`\`

---

## 📡 Deployment on Google Cloud Run (Optional)

1. Enable Cloud Run and Cloud Storage in GCP  
2. Push Docker image to Google Container Registry  
3. Deploy with appropriate IAM permissions and environment variables

---

## ✅ Future Enhancements

- 🖼️ Add support for:
  - Image resizing
  - Format conversion (e.g., PNG to JPG)
  - Watermark/logo overlay
- 🧠 Integrate ML-based image enhancements
- 🔐 Authenticated endpoints for secured image access

---

## 👥 Contributors

- **You!** Contributions, suggestions, and forks are welcome!

---

## 📃 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🌐 Example Public URL

\`\`\`
https://storage.googleapis.com/my-image-processor-bucket/processed/sample_processed.jpg
\`\`\`

---

> Built with ❤️ using Flask and Google Cloud for modern cloud-based workflows.
