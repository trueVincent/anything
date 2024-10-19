# anything

![Build Status](https://github.com/trueVincent/anything/actions/workflows/deploy.yml/badge.svg)
![Coverage](https://github.com/trueVincent/anything/blob/main/todo/coverage/coverage_badge.svg)

This is a repo to practice various tech stack so name it to "anything".
Tech stack:
- Django
- PostgreSQL
- Container(Docker and K8S)
- Redis
- RabbitMQ
- CI/CD(Jenkins or ...?)
- AWS
- Infra as code(Ansible/Terraform)
- Monitor(Grafana)
- Testing

## How to start the server
- Method 1: start db with Docker and start app with "python manage.py runserver" for local development.
  - "docker run --name todo-db --network todo -p 5432:5432 -v todo-db-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -d postgres"
  - create schema todo
  - "docker exec -it todo-db psql -U postgres"
  - "python manage.py runserver"
- Method 2: start db, app and nginx with Docker
  - Docker Network
    - Create bridge network "docker network create todo"
  - Database
    - "docker pull postgres"
    - "docker run --name todo-db --network todo -p 5432:5432 -v todo-db-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -d postgres"
    - create schema todo
    - "docker exec -it todo-db psql -U postgres"
  - App
    - "docker build -t todo-app ."
    - "docker run --name todo-app --network todo -p 8000:8000 -d todo-app"
  - Nginx
    - "docker build -t todo-nginx ."
    - "docker run --name todo-nginx --network todo -p 80:80 -d todo-nginx"
- Method 3: start db, app and nginx on AWS EC2 with Docker
  - Start an instance and get SSH private key file.
  - ssh to the server "ssh -i ./aws-key.pem ubuntu@13.208.193.116" and below happens on ec2.
  - Generate SSH key pairs for GitHub repo. Add public key to repo.
  - Start ssh-agent "eval "$(ssh-agent -s)""
  - Add GitHub ssh key "ssh-add ~/.ssh/id_rsa"
  - Clone the repo "git clone git@github.com:trueVincent/anything.git"
  - Add permission to script "chmod +x ./deployment/deploy_aws.sh" "chmod +x ./deployment/start_services.sh"
  - Execute deployment script "sudo bash ./deployment/deploy_aws.sh"
- Method 4: Similar to Method 3, but only use init-instance.sh when starting a new instance. Also, use GitHub Actions for automatic deployment.
  - For first-time setup, add the AWS SSH private key to GitHub Secrets. Then, generate a GitHub key on EC2 and add it to GitHub SSH Keys.
