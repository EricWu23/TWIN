# Architecture: CI/CD for AI System

## Flow
GitHub → Actions → OIDC → AWS → Terraform → Infra

## Components
- GitHub Actions (orchestrator)
- OIDC + IAM Role (auth)
- Terraform (infra engine)
- AWS (runtime)

## Key Patterns
- Infra as Code
- Stateless deployment
- Multi-env isolation

## Principle
Code → Pipeline → Infra → Running System
