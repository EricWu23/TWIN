# Debug: Terraform IAM & State Issues

## Problem
Terraform apply failed with:
- Route53 AccessDenied
- ACM AccessDenied

## Root Cause
Missing IAM permissions:
- route53:ListHostedZones
- acm:RequestCertificate

## Fix
Attached:
- AmazonRoute53FullAccess
- AWSCertificateManagerFullAccess

## Key Learning
Terraform needs BOTH:
- Read permissions (data sources)
- Write permissions (resource creation)

## State Insight
Terraform is NOT transactional:
- Partial infra may exist after failure

## Debug Workflow
1. Read error → identify AWS API
2. Map to IAM permission
3. Grant permission
4. Re-run `terraform apply`

## Takeaway
Infrastructure debugging = IAM + state + service API understanding