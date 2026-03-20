# Week 2 Day 2 – Key Learnings (AI Agent Production)

## 1. Architecture
- Frontend: S3 (static) + CloudFront (CDN)
- Backend: API Gateway → Lambda → FastAPI (ASGI via Mangum)
- Storage: S3 (memory), optionally local
- LLM: OpenAI / Bedrock

---

## 2. Request Flow
Browser → CloudFront → API Gateway → Lambda → FastAPI → LLM  
Response flows back same path.

---

## 3. ASGI vs Lambda
- FastAPI uses ASGI (`scope, receive, send`)
- Lambda uses `event, context`
- Mangum bridges them (no manual parsing needed)

---

## 4. CORS (Critical)
- Must match **exact origin** (no trailing `/`)
- API Gateway CORS overrides backend
- Preflight = `OPTIONS` request
- Failure often due to:
  - missing OPTIONS handling
  - origin mismatch
  - non-200 response

---

## 5. API Gateway
- Routes map HTTP → Lambda
- `/{proxy+}` = catch-all routing
- `OPTIONS` needed for CORS preflight
- Stages = environments (dev/test/prod)

---

## 6. CloudFront vs S3
- S3 = source of truth (immediate updates)
- CloudFront = cached (stale until invalidated)
- `/*` invalidation = one-time cache purge

---

## 7. Deployment Insights
- Docker used to build Lambda-compatible packages
- Use `manylinux2014_x86_64` for binary compatibility
- Avoid compiling dependencies in Lambda

---

## 8. Debugging Lessons
- “CORS error” often = preflight failure
- Check:
  - OPTIONS response
  - status code (must be 200)
  - correct origin
- Use `curl -X OPTIONS` to debug

---

## 9. Key Pitfalls
- Trailing `/` in origin breaks CORS
- CloudFront cache hides updates
- Wrong origin in CloudFront
- API Gateway overriding headers

---

## 10. Big Picture
> Most production AI work is not the model — it's infra, networking, and deployment.

---

## TL;DR
- CORS must match exactly
- API Gateway controls preflight
- CloudFront caches aggressively
- Mangum adapts FastAPI to Lambda
- Debugging = understand full request path
