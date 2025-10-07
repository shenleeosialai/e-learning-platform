# Use a stable, lightweight Python base
FROM python:3.12-slim-bookworm

# Prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install system dependencies required for uwsgi, cffi, and psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Make sure wait-for-it.sh is executable
RUN chmod +x /code/wait-for-it.sh

# Copy Django project files
COPY . .
