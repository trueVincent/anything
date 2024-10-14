#!/bin/bash

# Install Docker
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
echo "Install Docker complete"

# Create docker network
sudo docker network create todo

# Create DB and schema
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