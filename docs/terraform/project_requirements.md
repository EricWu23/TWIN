# Project Requirements

## Functional
- Chat with AI agent
- Persistent memory
- Web UI

## Non-Functional
- Scalable
- Secure
- Low latency

## Infrastructure
- S3 (frontend + memory)
- CloudFront (CDN)
- API Gateway
- Lambda
- Bedrock
- Route53 + ACM

## DevOps
- Terraform IaC
- Multi-environment support
- Version control

## Constraints
- ACM must be in us-east-1
- IAM permissions required for all resources

## Success Criteria
- One-command deployment
- No manual infra setup
- Fully reproducible environments