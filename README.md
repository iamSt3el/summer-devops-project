# Student Task Manager - DevOps Project

A modern Flask web application for managing student tasks with complete DevOps pipeline implementation.

## Features
- Create, update, and delete tasks
- Priority levels (High, Medium, Low)
- Task status tracking (Pending, In Progress, Completed)
- Real-time statistics
- Responsive design with Bootstrap
- REST API endpoints
- Health check endpoint

## DevOps Implementation

### 1. Git and GitHub
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Docker Commands
```bash
# Build Docker image
docker build -t student-task-manager:v1 .

# Run container
docker run -d -p 5000:5000 --name task-manager student-task-manager:v1

# Using Docker Compose
docker-compose up -d
docker-compose down
```

### 3. Kubernetes Commands
```bash
# Apply all manifests
kubectl apply -f k8s/

# Check deployments
kubectl get pods -n student-tasks
kubectl get services -n student-tasks
kubectl get deployments -n student-tasks

# Scale deployment
kubectl scale deployment student-task-manager --replicas=5 -n student-tasks

# Port forwarding
kubectl port-forward service/student-task-manager-service 8080:80 -n student-tasks

# Check logs
kubectl logs -l app=student-task-manager -n student-tasks
```

### 4. Minikube Setup
```bash
# Start minikube
minikube start

# Enable ingress
minikube addons enable ingress

# Build image in minikube
eval $(minikube docker-env)
docker build -t student-task-manager:latest .

# Access service
minikube service student-task-manager-service -n student-tasks
```

### 5. GCP/GKE Commands
```bash
# Create GKE cluster
gcloud container clusters create student-tasks-cluster --num-nodes=3

# Get credentials
gcloud container clusters get-credentials student-tasks-cluster

# Build and push to Container Registry
docker tag student-task-manager:latest gcr.io/YOUR_PROJECT_ID/student-task-manager:latest
docker push gcr.io/YOUR_PROJECT_ID/student-task-manager:latest
```

## Project Structure
```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container definition
├── docker-compose.yaml   # Multi-container setup
├── .github/
│   └── workflows/
│       └── ci.yaml       # CI/CD pipeline
├── k8s/                  # Kubernetes manifests
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
└── templates/            # HTML templates
    ├── base.html
    └── index.html
```