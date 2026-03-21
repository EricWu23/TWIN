# 🧠 [AI Digital Twin (Production-Ready)](https://yujiangwu-digitaltwin.com/)

This is a production-grade AI Digital Twin system built with **AWS Bedrock + Serverless + Terraform + CI/CD**.

Feel free to go to [https://yujiangwu-digitaltwin.com/](https://yujiangwu-digitaltwin.com/) to chat with me about my career and education.

---

## 🚀 Overview

This project implements a fully serverless AI application that:
- Serves a web-based AI assistant
- Maintains conversation memory
- Deploys infrastructure via Infrastructure-as-Code (Terraform)
- Supports multi-environment (dev / test / prod)
- Is CI/CD-ready with GitHub Actions

---

## 🏗️ Architecture
```txt

User (Browser)
↓
CloudFront (CDN)
↓
S3 (Frontend)
↓
API Gateway
↓
Lambda (FastAPI + Mangum)
↓
Bedrock (Nova Lite LLM)
↓
S3 (Conversation Memory)
```

---

## ⚙️ Tech Stack

Frontend: Next.js  
Backend: FastAPI + Lambda + Mangum  
AI: AWS Bedrock (Nova Lite)  
Infra: Terraform + AWS (S3, API Gateway, Lambda, CloudFront, Route53, ACM)  
DevOps: Git + GitHub Actions (next)

---

## 🔥 Key Features

- Serverless architecture
- Infrastructure as Code (Terraform)
- Multi-environment (dev/test/prod)
- HTTPS via ACM + CloudFront
- Persistent memory (S3)
- Global CDN delivery

---

## 🧠 What I Learned

- Terraform (providers, state, workspaces)
- IAM debugging (Route53, ACM)
- Serverless system design
- CloudFront + ACM constraints (us-east-1)
- Full-stack debugging (Frontend → Backend → AWS)

---

## 📦 Terraform Structure
```txt

terraform/
  main.tf
  variables.tf
  outputs.tf
  versions.tf
  terraform.tfvars
  prod.tfvars
```

---

## 🚀 Deployment

terraform init  
terraform apply  

Destroy:
terraform destroy

---

## ⚠️ Notes

- ACM must be in us-east-1 for CloudFront
- Terraform is idempotent (no duplicate infra)
- Not transactional (partial infra possible)

---

## 📈 Future Work

- CI/CD with GitHub Actions
- RAG (vector DB)
- Tool-based agents
- Observability

---

## 🎯 One-line Summary

Production-grade serverless AI system using Terraform + AWS Bedrock.
