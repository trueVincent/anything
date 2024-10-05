#!/bin/bash
# Ubuntu

# Install Docker
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Start services. e.g. db, app, nginx
sudo . ./deployment/start_services.sh