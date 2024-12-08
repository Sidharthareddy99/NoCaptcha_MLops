FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install the dependencies
RUN apt update && apt install awscli -y

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container


# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python3", "app.py"]