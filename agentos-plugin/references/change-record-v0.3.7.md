# AgentOS change record — 0.3.7

## Affected behavior

- Adds a no-retry rule for HeyGen generation routes blocked by plan or region.
- Allows direct Avatar Video as a fallback only when a fixed-background presenter still meets the requested outcome.
- Records the currently observed 5,000-character direct-avatar script limit and calls for shortening or segmenting before submission.

## Evidence

HeyGen Video Agent returned a non-retryable plan restriction for the connected free plan in this region. A subsequent direct Avatar Video request was accepted after reducing its script below 5,000 characters; an initial longer input was rejected before a video job was created.

## Compatibility

Plan availability and field limits can change. Check the live tool response and never invent a reset time. The fallback is conditional and must not silently remove required B-roll or other acceptance criteria.

## Rollback

Restore the 0.3.6 plugin release or revert the 0.3.7 source changes.
