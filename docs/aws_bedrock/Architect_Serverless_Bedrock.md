# Architect_Serverless_Bedrock

## Architecture Overview

```txt
User Browser
↓ HTTPS
CloudFront (CDN)
↓
S3 (Frontend)
↓ HTTPS API Calls
API Gateway
↓
Lambda (Backend)
├── Bedrock (AI inference)
└── S3 (memory storage)
```

## Design Principles
- Serverless (no infra management)
- Edge delivery (CloudFront)
- Fully AWS-native

## Benefits
- Low latency
- Scalable (Lambda auto-scale)
- Secure (IAM)
- Cost-efficient (pay-per-use)

## Tradeoffs
- Cold starts (Lambda)
- Debugging complexity
- Vendor lock-in (AWS)

## Key Decisions
- Use API Gateway instead of direct Lambda URL
- Use Bedrock instead of external APIs
- Store memory in S3 (simple persistence)

## Future Improvements
- Add caching layer (Redis)
- Add auth (Cognito)
- Add observability (X-Ray)
