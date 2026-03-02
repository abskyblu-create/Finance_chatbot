# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fly will send traffic to this port
ENV PORT=8080

# Start production server using Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "flask_app:app"]
