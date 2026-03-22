# System Design: AI CI/CD Pipeline

## Goal
Fully automated AI infra deployment

## Pipeline
git push →
GitHub Actions →
assume role (OIDC) →
terraform apply →
deploy frontend/backend

## Components
- GitHub (trigger)
- Actions (compute)
- Terraform (state mgmt)
- AWS (infra)

## Tradeoffs
+ Automation
+ Reproducibility
- Complexity
- Debug difficulty

## Reliability
- Idempotent Terraform
- State locking

## Security
- No static credentials
- Role-based access
