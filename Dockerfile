# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Expose the port your app runs on
EXPOSE 8080

# Start the Flask app
CMD ["python", "app.py"]

