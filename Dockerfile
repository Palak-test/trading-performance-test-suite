# Dockerfile

# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY loopa/ ./loopa/
COPY examples/ ./examples/
COPY pytest_loopa/ ./pytest_loopa/
COPY README.md ./
COPY LICENSE ./

# Install dependencies
RUN pip install --no-cache-dir pytest

# Default command
CMD ["python", "-m", "loopa"]
