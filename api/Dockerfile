# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/scripts:${PATH}" \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Run the command to start the app
CMD ["sh", "-c", "flask db init && flask db migrate && flask db upgrade && gunicorn --bind 0.0.0.0:5000 app:app"]
