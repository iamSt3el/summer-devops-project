# Student Task Manager - DevOps Project

A modern Flask web application for managing student tasks with complete DevOps pipeline implementation.

## 🌐 Live Application
**URL:** [http://student-task-manager.duckdns.org](http://student-task-manager.duckdns.org)  
**HTTPS:** [https://student-task-manager.duckdns.org](https://student-task-manager.duckdns.org)

Deployed on AWS EC2 with automated CI/CD pipeline using GitHub Actions.

## Features
- Create, update, and delete tasks
- Priority levels (High, Medium, Low)
- Task status tracking (Pending, In Progress, Completed)
- Real-time statistics
- Responsive design with Bootstrap
- REST API endpoints
- Health check endpoint

## DevOps Implementation

### 🚀 CI/CD Pipeline
Automated deployment using GitHub Actions with the following stages:
- **Test**: Python syntax and Flask app validation
- **Build**: Docker image creation and testing
- **Deploy**: Automated deployment to AWS EC2
- **Health Check**: Verification of successful deployment

### 🐳 Docker
```bash
# Build Docker image
docker build -t student-task-manager:v1 .

# Run container locally
docker run -d -p 5000:5000 --name task-manager student-task-manager:v1

# Using Docker Compose
docker-compose up -d
docker-compose down
```

### ☁️ AWS EC2 Deployment
- **Instance**: Amazon Linux 2 on EC2
- **Domain**: student-task-manager.duckdns.org
- **SSL**: Let's Encrypt certificates via Certbot
- **Ports**: HTTP (80), HTTPS (443), SSH (22)
- **Auto-scaling**: Container restart on deployment

### 🔧 Local Kubernetes Development
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
```

## Project Structure
```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container definition with HTTPS support
├── docker-compose.yaml   # Multi-container setup
├── .github/
│   └── workflows/
│       └── ci.yaml       # GitHub Actions CI/CD pipeline
├── k8s/                  # Kubernetes manifests (for local dev)
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
└── templates/            # HTML templates
    ├── base.html
    └── index.html
```

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap CSS
- **Containerization**: Docker
- **Orchestration**: Kubernetes (local development)
- **Cloud**: AWS EC2
- **CI/CD**: GitHub Actions
- **SSL**: Let's Encrypt (Certbot)
- **Domain**: DuckDNS
- **Registry**: Docker Hub

## 📈 Monitoring & Health
- Health check endpoint: `/health`
- Container health monitoring
- Automated deployment verification
- SSL certificate auto-renewal