# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY lmapp/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install specific versions of PyTorch, torchvision, and torchaudio
RUN pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu

# Install specific version of numpy
RUN pip install numpy==1.26.4

# Copy the application code
COPY lmapp /app/lmapp

# Set PYTHONPATH to ensure Python can find your modules
ENV PYTHONPATH=/app

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "lmapp.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
