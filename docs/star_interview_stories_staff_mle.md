# STAR Interview Stories – Staff MLE Level

## Story 1 — Leadership + Ownership
### Driving End-to-End AI Agent Deployment Under Ambiguity

**Situation**  
We needed to deploy a production-like AI consultation assistant combining frontend, backend, and LLM inference, but there was no clear standard architecture.

**Task**  
Own the design and delivery of a scalable, production-grade system.

**Action**  
- Designed: CloudFront → API Gateway → Lambda → FastAPI → LLM  
- Used Mangum to bridge ASGI with Lambda  
- Evaluated Vercel vs AWS tradeoffs  
- Defined clear infra boundaries  
- Documented system design  

**Result**  
- Delivered production-style system  
- Created reusable architecture patterns  
- Reduced ambiguity across decisions  

---

## Story 2 — Ownership + Failure
### Debugging a Production-Blocking CORS Issue

**Situation**  
Frontend failed due to CORS errors despite backend working.

**Task**  
Identify and resolve root cause quickly.

**Action**  
- Traced full request path  
- Identified preflight (OPTIONS) failure  
- Found root cause: trailing slash in origin  
- Fixed exact origin match  

**Result**  
- Restored system immediately  
- Established CORS debugging playbook  

---

## Story 3 — Conflict + Leadership
### Resolving Vercel vs AWS Architecture Decision

**Situation**  
Team debated between Vercel simplicity vs AWS control.

**Task**  
Drive alignment on architecture.

**Action**  
- Framed decision around requirements  
- Clarified backend limitations of Vercel  
- Positioned hybrid approach  

**Result**  
- Achieved alignment  
- Enabled scalable architecture decisions  

---

## Story 4 — Innovation
### Introducing Serverless AI Agent Architecture

**Situation**  
Traditional deployments required heavy infra management.

**Task**  
Design scalable, low-ops architecture.

**Action**  
- Proposed serverless pattern  
- Used Lambda + API Gateway + CloudFront  
- Eliminated server management  

**Result**  
- Reduced operational overhead  
- Achieved automatic scaling  

---

## Story 5 — Failure + Ownership
### Fixing CloudFront Cache Staleness

**Situation**  
Frontend updates not reflected after deployment.

**Task**  
Identify why users saw stale UI.

**Action**  
- Diagnosed CDN caching issue  
- Invalidated CloudFront cache (`/*`)  

**Result**  
- Restored correct UI  
- Established CDN debugging rule  

---

## Story 6 — Leadership + Innovation
### Turning Learnings into Reusable Systems

**Situation**  
Learning was not being leveraged long-term.

**Task**  
Create compounding system for knowledge reuse.

**Action**  
- Converted work into STAR stories  
- Created system design docs  
- Built reusable templates  

**Result**  
- Improved interview readiness  
- Built long-term knowledge leverage  

---

## TL;DR

- Leadership = reduce ambiguity  
- Ownership = full system responsibility  
- Conflict = align via tradeoffs  
- Failure = root cause + prevention  
- Innovation = reusable patterns
