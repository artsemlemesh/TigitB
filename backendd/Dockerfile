FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Upgrade pip and install wheel
RUN pip install --upgrade pip
RUN pip install wheel

# Install Python dependencies
RUN pip install -r requirements.txt

# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput
# Copy the rest of the application code into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
# CMD ["gunicorn", "gym_app.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
