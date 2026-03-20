# System_Design_AI_Chat_Serverless

## Problem
Design a scalable AI chat application.

## Requirements
- Low latency
- Scalable
- Secure
- Persistent memory

## High-Level Design
Client → CDN → Frontend → API → Compute → AI Model

## Detailed Design
- CloudFront: CDN
- S3: static frontend
- API Gateway: routing + auth
- Lambda: business logic
- Bedrock: AI inference
- S3: chat memory

## Scaling
- Lambda auto-scales
- API Gateway handles spikes
- CloudFront caches static assets

## Bottlenecks
- Bedrock latency
- Lambda cold start

## Optimizations
- Warm Lambdas
- Cache responses
- Stream responses

## Reliability
- Retry logic
- Logging (CloudWatch)
- Monitoring (metrics)

## Security
- IAM roles
- CORS control
- API Gateway auth

## Tradeoffs
- Simplicity vs control
- Serverless vs containers
