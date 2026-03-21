# Architecture: Terraform Multi-Environment AWS Deployment

## Overview
Single codebase → multiple environments (dev / prod)

## Components
- S3 → frontend hosting
- CloudFront → CDN
- API Gateway → routing
- Lambda → backend
- Bedrock → LLM
- S3 → memory
- Route53 → DNS
- ACM → SSL

## Key Pattern
Terraform:
- main.tf → resources
- variables.tf → inputs
- outputs.tf → outputs
- *.tfvars → environment config

## Multi-Region Design
- Default provider → us-east-2
- Alias provider → us-east-1 (ACM)

## Flow
User → CloudFront → S3/API → Lambda → Bedrock/S3

## Principle
Same architecture, different configs → isolated environments