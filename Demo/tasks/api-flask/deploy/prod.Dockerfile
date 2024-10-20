# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt test_requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt -r test_requirements.txt

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]