# Start with the Python 3.11 slim-bullseye base image
FROM python:3.11.6-slim-bullseye

# Set the PYTHONUNBUFFERED environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED=1

# Update the system and install necessary dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the working directory
COPY . /app/

# Expose any necessary ports (if applicable)
# EXPOSE 8000

# Set the default command to run when the container starts
CMD python manage.py runserver 0.0.0.0:8000