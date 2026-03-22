# Debug: CI/CD + IAM + OIDC

## Issues Encountered
- Route53 AccessDenied
- ACM AccessDenied
- Workflow not triggering
- Wrong folder (.github/workflow vs workflows)

## Root Causes
- Missing IAM permissions
- Wrong branch trigger
- Incorrect folder naming

## Fix Pattern
1. Read error
2. Map to AWS API
3. Add permission
4. Re-run pipeline

## Key Insight
CI/CD failures are usually:
IAM + config + path issues
