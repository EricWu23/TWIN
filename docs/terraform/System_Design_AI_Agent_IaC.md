# System Design: AI Agent with Terraform (Staff Level)

## Goal
Deploy scalable AI agent with IaC

## Architecture
Frontend:
- S3 static site
- CloudFront CDN

Backend:
- API Gateway
- Lambda (FastAPI + Mangum)

AI Layer:
- AWS Bedrock

Memory:
- S3 bucket

## Infra Layer
Terraform manages:
- provisioning
- updates
- destruction

## Key Design Decisions
1. Serverless → cost efficient
2. CDN → low latency
3. S3 memory → simple persistence
4. Multi-env → dev/prod isolation

## Tradeoffs
+ Simple
+ Scalable
- Cold start (Lambda)
- Limited long-running support

## Scalability
- CloudFront global
- Lambda auto-scale

## Reliability
- Stateless backend
- Persistent memory in S3

## Security
- IAM roles
- CORS control

## Staff Insight
IaC = system design translated into code