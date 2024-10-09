#!/bin/bash
# Ubuntu

# Install Docker
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
echo "Install Docker complete"
newgrp docker

# Start services. e.g. db, app, nginx
echo "start service"
sudo bash ./deployment/start_services.sh
echo "start service complete"