# Use the official Python image
FROM python:3.9-slim

# Copy the application code to the container
COPY app.py /app.py

# Set the working directory
WORKDIR /

# Install any dependencies (none in this case)
# RUN pip install -r requirements.txt

# Set the stop signal to SIGINT (default is SIGTERM)
STOPSIGNAL SIGINT

# Run the application
CMD ["python", "app.py"]
