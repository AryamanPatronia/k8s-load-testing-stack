# Cloud Computing Coursework – Kubernetes Load Testing & Monitoring

**Coursework for CSC8110 – Cloud Computing (Newcastle University)**  
Author: Aryaman Patronia  

---

## Project Overview
This project explores **cloud-native deployment and monitoring** using Kubernetes.  
The work focused on deploying applications, setting up monitoring tools, and benchmarking system performance under load.

---

## What Was Done
- Deployed the **Kubernetes Dashboard** using Helm and accessed it securely.  
- Deployed a sample web application (`nclcloudcomputing/javabenchmarkapp`) with Kubernetes.  
- Exposed the app via a **NodePort service** for external access.  
- Set up a full **monitoring stack** (Prometheus, metrics server, Grafana) inside Kubernetes.  
- Verified metrics collection and visualized data in Grafana dashboards.  
- Developed a **Python Load Generator** that:  
  - Sends configurable web requests to a target service  
  - Collects metrics: **average response time** and **failures**  
  - Packaged as a **Docker image** and pushed to a local registry  
- Deployed the load generator as a **Kubernetes deployment**.  
- Benchmarked CPU and memory usage of the web app under load using Grafana panels.  

---

## Key Learning Outcomes
- Hands-on experience with **Kubernetes deployments, services, and monitoring stacks**.  
- Understanding of how to integrate **Prometheus + Grafana** for system observability.  
- Practical experience in building a **custom load testing tool** and running it in Kubernetes.  
- Benchmarking applications for performance under varying load.  

---

## Repository Contents
- `LoadGenerator.py` – Python script for load generation  
- `Dockerfile` – Containerization of the load generator  
- `deployment.yaml` – Kubernetes manifest for running the load generator  
- `report.pdf` – Full coursework report with details and screenshots  

---
