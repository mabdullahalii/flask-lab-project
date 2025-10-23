# Use the official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirement file first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose Flask’s default port
EXPOSE 5000

# Default command — runs the Flask app
CMD ["python", "app.py"]
