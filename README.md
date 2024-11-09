# anything

![Build Status](https://github.com/trueVincent/anything/actions/workflows/deploy.yml/badge.svg)
![Coverage](https://github.com/trueVincent/anything/blob/main/todo/coverage/coverage_badge.svg)

## Table of Contents
- [Project Initiation](#project-initiation)
- [High Level Design](#high-level-design)
- [Deployment](#deployment)
  - [Development](#deployment-development)
  - [Container](#deployment-container)
  - [Cloud+Scripting](#deployment-cloud)
  - [CI/CD](#deployment-cicd)
  - [Kubernetes](#deployment-kubernetes)
- [How Does the Coverage Badge Work Without Third-Party Services (e.g., Codecov)?](#coverage-badge)
- [APIs](#apis)

<a name="project-initiation" id="project-initiation"></a>
## Project Initiation
This project is designed to practice various DevOps skills and can encompass a range of technologies, hence the name "anything."  
The primary focus areas are **cloud (AWS), CI/CD (GitHub Actions), and containerization (Docker and Kubernetes)**. Additionally, the project utilizes the following tech stack: **Django, PostgreSQL, Nginx, and testing tools**

<a name="high-level-design" id="high-level-design"></a>
## High Level Design
**Client** - **AWS EC2 Instance** - **Reverse Proxy/Load Balancer(Nginx)** - **App Servers(Gunicorn and Django)** - **Database(PostgreSQL)**

<a name="deployment" id="deployment"></a>
## Deployment
<a name="deployment-development" id="deployment-development"></a>
- **Method 1: Local Development.** Start DB with Docker and start app with `python manage.py runserver` for local development.
  - `docker run --name todo-db --network todo -p 5432:5432 -v todo-db-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -d postgres`
  - Create DB schema
  - `python manage.py runserver`
<a name="deployment-container" id="deployment-container"></a>
- **Method 2: Container.** Start DB, app and Nginx with Docker
  - Docker Network
    - Create bridge network `docker network create todo`
  - Database
    - `docker pull postgres`
    - `docker run --name todo-db --network todo -p 5432:5432 -v todo-db-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123456 -d postgres`
    - create DB schema
  - App
    - `docker build -t todo-app .`
    - `docker run --name todo-app --network todo -p 8000:8000 -d todo-app`
  - Nginx
    - `docker build -t todo-nginx .`
    - `docker run --name todo-nginx --network todo -p 80:80 -d todo-nginx`
<a name="deployment-cloud" id="deployment-cloud"></a>
- **Method 3: Cloud with Shell Script.** Start DB, app and Nginx on AWS EC2 with Docker
  - Start an instance and get SSH private key file.
  - SSH to the server `ssh -i ./aws-key.pem ubuntu@15.168.7.0` and below happens on EC2.
  - Generate SSH key pairs for GitHub repo. Add public key to repo.
  - Start ssh-agent `eval "$(ssh-agent -s)"`
  - Add GitHub ssh key `ssh-add ~/.ssh/id_rsa`
  - Clone the repo `git clone git@github.com:trueVincent/anything.git`
  - Add permission to script `chmod +x ./deployment/deploy_aws.sh` `chmod +x ./deployment/start_services.sh`
  - Execute deployment script `sudo bash ./deployment/deploy_aws.sh`
<a name="deployment-cicd" id="deployment-cicd"></a>
- **Method 4: Auto CI/CD.** Similar to Method 3, but only use init-instance.sh when starting a new instance. Also, use GitHub Actions for automatic deployment.
  - For first-time setup, add the AWS SSH private key to GitHub Secrets. Then, generate a GitHub key on EC2 and add it to GitHub SSH Keys.
  - Stage Build: Build Django and Nginx Docker images and run database migration.
  - Stage Test: Execute test, check coverage and generate coverage badge.
  - Stage Deploy
<a name="deployment-kubernetes" id="deployment-kubernetes"></a>
- **Method 5: Kubernetes.**
  - Database Deployment: Configure a PersistentVolume and PersistentVolumeClaim to keep database data outside the pods. Set the service type to ClusterIP for internal communication between pods.
  - Application Deployment: Configure a PersistentVolume and PersistentVolumeClaim to share static files outside the pods. Set the service type to ClusterIP for internal communication between pods.
  - Nginx Deployment: Use a PersistentVolumeClaim to serve Django static files. Set the service type to NodePort to expose Nginx externally. Optionally, add a LoadBalancer or Ingress for future scalability and traffic management.
  - Build and push Docker images.
    - `cd deployment/k8s`
    - `docker build -f app/app-Dockerfile -t 39215068/todo-app:1.2 ../../todo`
    - `docker push 39215068/todo-app:1.2`
    - `docker build -f nginx/nginx-Dockerfile -t 39215068/todo-nginx:2.2 ./nginx`
    - `docker push 39215068/todo-nginx:2.2`
  - Apply
    - `kubectl apply -f db/`
    - `kubectl apply -f app/`
    - `kubectl apply -f nginx/`
  - Check status of running pods
    - `kubectl get pods`
  - All yaml files are in the `deployment/k8s` folder

<a name="coverage-badge" id="coverage-badge"></a>
## How Does the Coverage Badge Work Without Third-Party Services(e.g. Codedev)?
- Generate a test report using the Python `coverage` library.
- Generate a test coverage badge using the Python `coverage-badge` library.
- Upload the coverage badge to the main branch and use it to display the badge in the `README.md`.
- For implementation details, see `test.sh` and `deploy.yml`.

<a name="apis" id="apis"></a>
## APIs
This project provides basic RESTful APIs for CRUD operations on Todo objects as a demonstration.  
- **GET** `/api/v1/todos/`  
  Retrieves a list of todo items.  
  **Headers**: `{"Authorization": "JWT Token"}`
- **POST** `/api/v1/todos/`  
  Creates a new todo item.  
  **Headers**: `{"Authorization": "JWT Token"}`  
  **Data**: `{"title": "Buy sugar", "description": "Buy 1 get 1 free", "completed": false}`
- **PUT** `/api/v1/todos/{pk}/`  
  Updates an existing todo item by primary key ({pk}).  
  **Headers**: `{"Authorization": "JWT Token"}`  
  **Data**: `{"title": "Buy sugar", "description": "Buy 1 get 1 free", "completed": true}`
- **DELETE** `/api/v1/todos/{pk}/`  
  Deletes a todo item by primary key ({pk}).  
  **Headers**: `{"Authorization": "JWT Token"}`
