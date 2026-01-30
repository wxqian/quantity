FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
# build-essential for compiling some python packages if wheels are missing
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy configuration files
COPY pyproject.toml README.md ./

# Install dependencies
# Using pip to install from pyproject.toml
RUN pip install --no-cache-dir .

# Copy application code
COPY qtf ./qtf
COPY main.py .

# Environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "main.py"]
