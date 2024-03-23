# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code to the working directory
COPY . .

# Run the Python application
CMD ["python", "main.py"]
