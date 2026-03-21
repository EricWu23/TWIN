# Interview Story: Terraform Deployment & Debugging

## Situation
I deployed a production AI system using Terraform across multiple AWS services.

## Task
Ensure fully automated deployment with:
- multi-environment support
- secure infrastructure
- reproducibility

## Action
- Designed Terraform modules for full stack
- Implemented provider alias for cross-region (ACM us-east-1)
- Used tfvars for env separation
- Debugged IAM issues:
  - Route53 AccessDenied
  - ACM AccessDenied

## Result
- Achieved one-command deployment
- Eliminated manual infra setup
- Reduced deployment errors significantly

## Learning
- Terraform requires both read/write IAM
- Infrastructure is not transactional → must handle partial state

## Leadership Angle
Drove infra standardization and reproducibility across environments