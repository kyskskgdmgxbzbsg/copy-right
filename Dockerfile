# Use Python 3.10 slim as base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file to container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the bot source code
COPY . .

# Run the bot
CMD ["python", "main.py"]