# Use official Python image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /home/piruby

# Install system dependencies in a single RUN layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    g++ \
    build-essential \
    nano \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add pg_config to PATH explicitly, if needed
ENV PATH=$PATH:/usr/bin

# Copy the rest of the application
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8007", "main:app", "--timeout", "180", "--workers", "2"]

