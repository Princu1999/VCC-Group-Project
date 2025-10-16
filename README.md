# Cloud Image Processing API (Flask + Google Cloud Storage)

A lightweight, cloud-ready image processing service with a simple REST API for **upload → process → store → fetch** workflows. Current operations include grayscale conversion, with an extensible hook for adding resize, format conversion, or watermarking. Built with **Flask** and designed to run locally, in Docker, or on **Google Cloud Run**.

---

## Live Demo

**Hugging Face Space:** https://huggingface.co/spaces/Princu1999/Cloud-Image-Processing-Service

---

## Demo Video


<video src="assets/VCC_Project_demo.mp4" controls width="720">
</video>


---

## Features

- Upload an image via API and apply basic processing (grayscale).
- Store processed outputs in **Google Cloud Storage** and get a **public URL**.
- Download processed images via API.
- One-file Flask app, minimal deps, **Docker-ready** for easy deployment.

---

## Project Structure

```
VCC-Group-Project/
├── app.py               # Flask app & routes
├── image_processor.py   # Processing + GCS helpers
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build
├── huggingface/         # Assets for Space/hosted demo
├── test_images/         # Sample input images
├── processed_image/     # Sample outputs (local)
└── assets/              # README media (hf_deploy.png, demo.mp4)
```

> Folder names reflect what’s currently present in the repository. Adjust if your layout changes.

---

## Quick Start

### 1) Local setup

```bash
# clone
git clone https://github.com/Princu1999/VCC-Group-Project.git
cd VCC-Group-Project

# python deps
pip install -r requirements.txt
```

Set required environment variables:

```bash
# path to your GCP service account key (JSON)
export GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/key.json"

# name of your existing GCS bucket
export BUCKET_NAME="your-bucket-name"
```

Run:

```bash
python app.py
# app listens on 0.0.0.0:8080 by default (adjust if needed)
```

> The service expects valid GCP credentials and an existing bucket.

---

## API

### Upload & Process

**POST** `/upload`  
Form-data: `image` (binary file)

**Response (JSON):**
```json
{
  "message": "Image processed successfully",
  "processed_image_url": "https://storage.googleapis.com/<your-bucket>/processed/<name>_processed.jpg"
}
```

**Example (curl):**
```bash
curl -X POST http://localhost:8080/upload \
  -F "image=@test_images/sample.jpg"
```

### Download

**GET** `/download?filename=<name>`  
Returns the image as an attachment if found.

**Example:**
```bash
curl -L "http://localhost:8080/download?filename=example_processed.jpg" \
  -o example_processed.jpg
```

> Endpoint names and response shapes match the current code. If you change function names or paths, update this section accordingly.

---

## Configuration

| Variable                         | Purpose                                        |
|----------------------------------|------------------------------------------------|
| `GOOGLE_APPLICATION_CREDENTIALS` | Absolute path to your GCP service account key  |
| `BUCKET_NAME`                    | Target Google Cloud Storage bucket name        |

---

## Docker

Build the image:

```bash
docker build -t cloud-image-service .
```

Run the container:

```bash
docker run -p 8080:8080 \
  -e BUCKET_NAME="your-bucket-name" \
  -e GOOGLE_APPLICATION_CREDENTIALS="/app/key.json" \
  -v "$(pwd)/key.json:/app/key.json" \
  cloud-image-service
```

> The provided `Dockerfile` and requirements are set up for a slim Python image that runs `app.py`.

---

## Deploying on Google Cloud Run (Optional)

1. Enable **Cloud Run** and **Cloud Storage** in your GCP project.  
2. Push your Docker image to Artifact/Container Registry.  
3. Deploy on Cloud Run, passing the two environment variables above and granting the service account permission to write to the bucket.  
4. Set **ingress** and **authentication** per your needs (public vs. private).

---

## Testing

- Use the sample files in `test_images/` with the curl commands above.  
- Add unit tests for `image_processor.py` (e.g., verifying grayscale transform and GCS upload stub).  
- Consider adding a GitHub Actions workflow to run linting and tests.

---

## Roadmap

- [ ] Add image **resize**, **format conversion**, and **watermark** options  
- [ ] Optional authentication for private buckets/routes  
- [ ] CI workflow and basic tests  
- [ ] Simple web UI for manual uploads

---

## Contributing

Issues and PRs are welcome! Please open an issue to discuss any non-trivial changes first.

---

## License

MIT — add a `LICENSE` file if missing.

---

### Acknowledgements

Built with ❤️ using **Flask** and **Google Cloud Storage**.
