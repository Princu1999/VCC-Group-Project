---
title: Cloud Image Processor
emoji: 🖼️
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.44.1
app_file: app.py
pinned: false
---

# ☁️ Cloud-based Image Processor

This is a Streamlit frontend for a Google Cloud Run-based image processing API.

- Upload **one or more images**
- Processed images are returned via the Cloud Run service
- Images are stored in Google Cloud Storage and served back via public URL

✅ **API Endpoint:** [Cloud Run](https://image-processor-service-365849256430.us-central1.run.app/upload)

✅ **How to use:**
1. Upload one or more images.
2. Wait for processing.
3. View and download your processed images!

🚀 Built with Streamlit + Google Cloud + Hugging Face Spaces