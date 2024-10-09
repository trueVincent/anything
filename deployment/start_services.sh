#!/bin/bash

# Function to stop and remove a container if it exists
function clean_container() {
    if [ "$(docker ps -aq -f name=$1)" ]; then
        echo "Stopping and removing existing container: $1"
        sudo docker stop $1
        sudo docker rm $1
    fi
}
# Clean up existing containers
clean_container todo-nginx
clean_container todo-app
clean_container todo-db

# Create bridge network
sudo docker network create todo

# Start PostgreSQL database
echo "Starting PostgreSQL database..."
sudo docker run --name todo-db --network todo -p 5432:5432 -v todo-db-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -d postgres:16
# # Wait for PostgreSQL to become available
echo "Waiting for PostgreSQL to initialize..."
until sudo docker exec todo-db pg_isready -U postgres; do
    sleep 1
done
# Create the schema "todo"
echo "Creating schema 'todo'..."
sudo docker exec todo-db psql -U postgres -c 'CREATE SCHEMA IF NOT EXISTS "todo";'

# Build and start the Django app service
echo "Building and starting Django app service..."
sudo docker build -t todo-app ./todo/.
sudo docker run --name todo-app --network todo -p 8000:8000 \
    -v /mnt/app-logs:/app/logs \
    -v /mnt/app-media:/mnt/media \
    -v /mnt/app-static:/mnt/static \
    -d todo-app
sudo docker exec todo-app python manage.py migrate

# Build and start Nginx
echo "Building and starting Nginx..."
sudo docker build -t todo-nginx ./deployment/nginx/.
sudo docker run --name todo-nginx --network todo -p 80:80 -d todo-nginx

echo "All services started successfully!"