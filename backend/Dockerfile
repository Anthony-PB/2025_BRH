# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application's code
COPY . .

# The command to run your application
# This uses Gunicorn, a production-grade WSGI server for Python
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]