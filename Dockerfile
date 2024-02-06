# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Gunicorn
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Start Gunicorn and serve the Flask app. Adjust the number of worker processes as needed.
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8080", "app:app"]