# Use a lightweight Python base image...
FROM python:3.9-slim

# Install curl because we use it in our LoadGenerator.py file for connectivity testing...
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set the working directory...
WORKDIR /app

# Copy Python script into our container...
COPY LoadGenerator.py .

# This will install the dependencies...(requests)
RUN pip install requests

# Setting the entry point for the container so it runs the LoadGenerator python script...
ENTRYPOINT ["python3", "LoadGenerator.py"]
