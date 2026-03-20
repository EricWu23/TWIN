# Debug_Bedrock_Integration

## Summary
Debugged a 400 error when migrating from OpenAI to AWS Bedrock.

## Problem
Frontend showed:
- "Failed to send message"
- HTTP 400 from API Gateway

## Investigation Steps
1. Checked Browser DevTools → Network → /chat → Response
2. Found error: "Invalid message format for Bedrock"
3. Checked Lambda logs (CloudWatch)
4. Found real error:
   - ValidationException
   - Model not supported for on-demand throughput

## Root Cause
Incorrect Bedrock model ID:
amazon.nova-2-lite-v1:0

## Fix
Changed to:
us.amazon.nova-2-lite-v1:0

## Key Learnings
- Always check backend logs (CloudWatch)
- DevTools only shows surface errors
- Bedrock models are region-specific
- 400 ≠ frontend issue

## Takeaway
Full-stack debugging requires tracing:
Frontend → API → Lambda → Bedrock
