# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Set environment variables


# Expose the port your app runs on
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate

# Define the command to start your app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]
