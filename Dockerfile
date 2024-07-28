# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pandas streamlit

# Expose the port the app runs on
EXPOSE 8501

# Default command for the container
CMD ["python", "main.py"]