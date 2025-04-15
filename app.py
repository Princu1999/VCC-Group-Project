# app.py

from flask import Flask, request, jsonify, send_file
import os
from image_processor import process_image_function, upload_to_bucket

app = Flask(__name__)
os.makedirs('processed_images', exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "Image Processing API is running!"}), 200

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    filename = image_file.filename
    processed_filename = f"{os.path.splitext(filename)[0]}_processed.jpg"
    output_path = os.path.join('processed_images', processed_filename)

    process_image_function(image_file, output_path)

    bucket_name = os.environ.get('BUCKET_NAME', 'my-image-processor-bucket')
    blob_name = f'processed/{processed_filename}'
    public_url = upload_to_bucket(blob_name, output_path, bucket_name)

    print(f"Using bucket: {bucket_name}")
    print(f"Uploading blob: {blob_name}")

    return jsonify({
        "message": "Image processed successfully",
        "processed_image_url": public_url
    }), 200

@app.route('/download', methods=['GET'])
def download_image():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    file_path = os.path.join('processed_images', filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, mimetype='image/jpeg', as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
