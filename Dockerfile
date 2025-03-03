# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy script and text files into the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create output directory
RUN mkdir -p /home/data/output

# Run the script when the container starts
CMD ["python", "script.py"]
