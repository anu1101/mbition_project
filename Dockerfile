# Use the official Python image as base image
FROM python:3-alpine3.15

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Install Flask and requests
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

# Command to run the Flask application
CMD python ./app.py
