# Interview_Story_Debugging_Bedrock

## Situation
While migrating an AI app from OpenAI to AWS Bedrock, the system returned 400 errors.

## Task
Identify and resolve the issue to restore functionality.

## Action
- Inspected browser DevTools → found 400 error
- Checked API Gateway → no clear issue
- Investigated Lambda logs in CloudWatch
- Found Bedrock ValidationException
- Identified incorrect model ID
- Updated to region-specific model ID

## Result
- System restored successfully
- Reduced debugging time in future incidents
- Improved understanding of AWS Bedrock

## Key Learnings
- Always check backend logs
- Cloud systems require multi-layer debugging
- Region configuration matters

## Impact
- Enabled full migration to AWS-native AI stack
- Improved reliability and observability
