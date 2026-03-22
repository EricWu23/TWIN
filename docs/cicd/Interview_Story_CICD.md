# Interview Story: CI/CD for AI System

## Situation
Manual deployment of AI system was error-prone and inconsistent.

## Task
Build automated deployment pipeline with secure authentication and multi-env support.

## Action
- Implemented GitHub Actions pipeline
- Configured OIDC authentication (no AWS keys)
- Set up Terraform remote state + locking
- Designed dev/test/prod workflows

## Result
- One-command deployment
- Eliminated manual errors
- Improved reproducibility and security

## Learning
- CI/CD is infra + security + orchestration
- IAM debugging is critical skill

## Impact
Enabled production-grade AI deployment workflow
