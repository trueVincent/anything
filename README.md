# anything
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
- Method 1: start db, app and nginx using docker command separately
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
- Method 2: docker-compose
