# AI Agent Production System Design (Interview Version)

## 1. Problem Statement

Design a production-grade AI agent platform that serves web users through a chat interface, supports short-term conversation memory, optional retrieval/tool use, and can be deployed safely across dev, test, and prod.

The system should:
- serve a static frontend globally
- expose a backend API for chat
- call an LLM provider
- persist conversation memory
- support CI/CD and infrastructure as code
- be observable, secure, and cost-aware

---

## 2. High-Level Architecture

```text
Users / Browser
      |
      v
CloudFront (CDN + TLS)
      |
      v
Static Frontend (S3)
      |
      | HTTPS / fetch
      v
API Gateway
      |
      v
Lambda (FastAPI via Mangum)
      |
      +--> Memory Store (S3 or DynamoDB)
      |
      +--> Retrieval / Tool layer (optional)
      |
      v
LLM Provider (Bedrock / OpenAI)

Supporting Plane:
- Terraform for infrastructure
- GitHub Actions for CI/CD
- CloudWatch for logs/metrics
- AWS Billing + Resource Explorer for cost/resource control
```

---

## 3. Core Request Flow

### Chat request
1. User opens the frontend through CloudFront.
2. Browser downloads static assets from CloudFront/S3.
3. User sends a message from the UI.
4. Frontend calls the backend API through API Gateway.
5. API Gateway transforms the HTTP request into a Lambda event.
6. Lambda invokes the FastAPI app through Mangum.
7. Backend:
   - loads session memory
   - builds prompt/context
   - calls the LLM
   - stores updated conversation
8. Response flows back:
   - FastAPI response
   - Mangum -> Lambda proxy response
   - API Gateway -> HTTP response
   - Browser renders the assistant answer

---

## 4. Why This Architecture

### Frontend on S3 + CloudFront
Use S3 for cheap static hosting and CloudFront for:
- global CDN delivery
- TLS termination
- lower latency
- cache distribution

### API Gateway + Lambda
Use serverless backend for:
- low ops overhead
- auto scaling
- pay-per-use economics
- natural fit for bursty traffic

### FastAPI + Mangum
Use FastAPI because it gives:
- clear routes
- typed request/response schema
- local development with Uvicorn
- easier extension for tools/RAG later

Use Mangum because Lambda expects `event/context`, while FastAPI is ASGI.

### S3 for memory
Use S3 initially because it is simple and cheap for per-session JSON history.
This can later evolve to DynamoDB or Redis if concurrency/latency needs grow.

---

## 5. API Design

### Endpoints
- `GET /`
  - sanity/root endpoint
- `GET /health`
  - health check
- `POST /chat`
  - main chat endpoint
- `GET /conversation/{session_id}`
  - debug / retrieval of stored session history

### Request schema
```json
{
  "message": "How does this system work?",
  "session_id": "optional-session-id"
}
```

### Response schema
```json
{
  "response": "Explanation...",
  "session_id": "session-id"
}
```

---

## 6. Memory Design

### Current design
- each session gets a `session_id`
- conversation is stored externally
- LLM remains stateless
- backend reconstructs context each turn

### Why this matters
LLMs do not remember prior turns unless history is explicitly re-sent.
So memory is a system feature, not a model feature.

### Current tradeoff
Simple approach:
- store JSON per session
- replay last N messages into prompt

Benefits:
- easy to reason about
- easy to debug
- simple deployment

Limitations:
- prompt grows with conversation
- no summarization yet
- not ideal for very long sessions

### Next-level evolution
- summarize old turns
- split short-term vs long-term memory
- move memory to DynamoDB/Redis
- attach retrieval and user profile memory

---

## 7. Prompt / Context Construction

The backend builds context from:
1. system prompt
2. optional persona / profile documents
3. prior conversation turns
4. current user query

This is the minimum viable form of context engineering.

Future upgrades:
- RAG retrieval
- tool outputs
- safety layers / guardrails
- prompt versioning

---

## 8. CORS and Networking

Because frontend and backend are on different origins, browser calls require CORS.

Key lessons:
- CORS origin must match exactly
- no trailing slash in origin
- browser sends preflight `OPTIONS` request
- API Gateway CORS can override backend CORS headers
- `OPTIONS` must return 200 and valid allow-* headers

Typical production configuration:
- frontend origin = exact CloudFront URL or custom domain
- allow credentials only when needed
- avoid `*` once moving to stricter production setup

---

## 9. CloudFront Caching

CloudFront caches static assets.
Important operational lesson:
- updating S3 does not immediately update CloudFront
- CloudFront may serve stale files until TTL expiry
- use invalidation (often `/*`) after deployment

Typical deployment sequence:
1. upload new frontend files to S3
2. invalidate CloudFront
3. next request fetches fresh content from origin

---

## 10. Deployment Strategy

### Local development
- Uvicorn for backend
- Next.js dev server for frontend
- local file memory
- `.env` for configuration

### Cloud deployment
- package Lambda artifact with dependencies
- use Docker to build Lambda-compatible dependencies
- deploy backend to Lambda
- deploy static frontend to S3
- expose frontend via CloudFront
- route backend through API Gateway

---

## 11. Why Docker Is Used in Lambda Packaging

The deployment package is built inside the Lambda Python runtime image to ensure:
- Linux compatibility
- x86_64 compatibility
- correct wheel resolution for binary packages

This avoids:
- Mac/Windows build mismatch
- local compilation issues
- runtime dependency failures in Lambda

---

## 12. Infrastructure as Code

Use Terraform to define:
- Lambda
- API Gateway
- S3 buckets
- CloudFront distribution
- IAM roles/policies
- Route53 / ACM for prod custom domain if needed

### Why Terraform
- reproducible
- reviewable
- version controlled
- safe across environments
- destroyable

### Environment model
Use workspaces or environment variables for:
- dev
- test
- prod

Naming pattern example:
- `twin-dev-api`
- `twin-test-api`
- `twin-prod-api`

---

## 13. CI/CD Design

Use GitHub Actions to automate deployment.

### Typical flow
```text
git push
  -> GitHub Actions
  -> setup Python / Node / Terraform
  -> build Lambda package
  -> terraform apply
  -> build frontend
  -> upload frontend to S3
  -> invalidate CloudFront
```

### Security model
Use OIDC + IAM role assumption instead of static AWS keys.

### Terraform state
Use:
- S3 bucket for remote Terraform state
- DynamoDB table for state locking

This enables:
- safe reruns
- team usage
- protection against concurrent state corruption

---

## 14. Observability

### Logs
CloudWatch logs for:
- Lambda execution
- FastAPI app errors
- deployment/debug traces

### Metrics
CloudWatch metrics for:
- Lambda invocations
- duration
- errors
- throttles
- Bedrock / LLM latency and token usage

### Operational dashboards
Track:
- response latency
- LLM usage
- error rate
- cost trend

---

## 15. Security Considerations

### Public vs private buckets
- frontend bucket: publicly readable objects for static site hosting
- memory bucket: private, backend-only access via IAM

### IAM
Use least privilege where practical:
- Lambda role: only what backend needs
- GitHub Actions role: only deployment permissions
- no long-lived credentials in repo

### CORS hardening
For demos, `*` may be fine.
For production, prefer exact allowed origins.

---

## 16. Cost Control

Use serverless to keep baseline cost low.

### Main cost levers
- Lambda invocations/duration
- API Gateway calls
- CloudFront egress
- LLM token usage
- S3 storage

### Cost hygiene
- destroy unused dev/test/prod environments
- inspect AWS Billing regularly
- use Resource Explorer to find orphan resources
- invalidate CloudFront only when needed
- use smaller LLMs for dev/test

---

## 17. Scaling Considerations

### Works well for:
- prototypes
- internal tools
- lightweight AI assistants
- moderate traffic with burstiness

### Pressure points as system grows:
- Lambda cold starts
- long-running tool workflows
- streaming complexity
- shared memory concurrency
- retrieval latency
- prompt growth

### Evolution path
As traffic and complexity grow, migrate backend to containerized FastAPI if needed:
- ECS / App Runner / Kubernetes
- better control over latency
- long-running workers
- richer streaming and background jobs

---

## 18. Main Tradeoffs

### Why Lambda first
Pros:
- fast to launch
- low ops
- scales automatically
- cost efficient for intermittent usage

Cons:
- cold starts
- execution limits
- less control

### Why containers later
Pros:
- stable latency
- better for streaming and multi-step agents
- richer background processing

Cons:
- more ops
- always-on cost
- higher infra complexity

---

## 19. Failure Modes and Mitigations

### 1. CORS failure
Cause:
- origin mismatch
- bad preflight handling
Mitigation:
- exact origin match
- explicit OPTIONS handling
- verify API Gateway CORS config

### 2. Stale frontend
Cause:
- CloudFront cache
Mitigation:
- invalidate distribution after upload

### 3. Dependency mismatch in Lambda
Cause:
- building packages on wrong platform
Mitigation:
- package inside Lambda runtime Docker image

### 4. Terraform drift/state problems
Cause:
- local-only state
Mitigation:
- remote state in S3 + DynamoDB lock

### 5. Rising LLM cost
Cause:
- large prompts / expensive model
Mitigation:
- smaller models in non-prod
- trim memory window
- summarize old turns

---

## 20. Interview Summary Answer

If asked to describe the design in 60 seconds:

> I would design the AI agent as a serverless web system. The frontend is a static site hosted on S3 and distributed globally through CloudFront. The backend is exposed through API Gateway and implemented as a FastAPI application running in Lambda via Mangum, which bridges Lambda's event model to ASGI. The backend loads session memory from S3, builds prompt context, calls an LLM provider such as Bedrock or OpenAI, stores the updated conversation, and returns the response to the client. Infrastructure is managed with Terraform across dev, test, and prod, deployment is automated through GitHub Actions using OIDC-based AWS authentication, and the system is monitored through CloudWatch with explicit cost and resource hygiene.

---

## 21. Strong Follow-up Points

If interviewer pushes deeper, emphasize:
- why CORS failed and how you debugged it
- why CloudFront invalidation matters
- why Mangum exists
- why Terraform remote state matters
- when you would move from Lambda to containers
- how you would add RAG / tools / memory summarization next
