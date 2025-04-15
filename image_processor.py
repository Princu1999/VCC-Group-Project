# image_processor.py

from PIL import Image
from google.cloud import storage
import os

def upload_to_bucket(blob_name, file_path, bucket_name):
    """Uploads a file to the bucket and returns the public URL."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        public_url = f"https://storage.googleapis.com/{bucket_name}/{blob_name}"
        print(f"File uploaded to {public_url}")
        return public_url
    except Exception as e:
        print(f"Error uploading to bucket: {e}")
        raise

def process_image_function(image_file, output_path):
    """Converts the uploaded image to grayscale and saves it."""
    try:
        image = Image.open(image_file)
        grayscale_image = image.convert("L")
        grayscale_image.save(output_path)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
        raise
