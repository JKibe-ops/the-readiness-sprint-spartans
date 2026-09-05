# Cross-Examination Prep

## Why Flask and SQLite?
**State:** We chose the smallest stack that proves the workflow. **Context:** One retailer operation and no mandated scale target. **Evidence:** The app runs as one Python process with one delivery table and a reproducible seed.

## What if two dispatchers assign the same rider?
**State:** The prototype does not fully solve concurrent assignment. **Context:** It has one current rider field and no locking workflow. **Evidence:** That is a known trade-off. Next: transactional assignment, unique active-shift constraints, and conflict feedback.

## What if the rider loses connectivity?
**State:** Offline updates are a roadmap item. **Context:** Polling requires connectivity and the current demo is online. **Evidence:** The sync label changes to Offline - retrying on request failure. Next: local queue plus idempotent replay.

## How do you know this is working?
**State:** We would measure operational outcomes, not feature count. **Context:** The current UI proves the path but has no production telemetry. **Evidence:** The first metrics are assignment time, completion rate, sync freshness, and proof capture rate.

## What don't you know yet?
**State:** We do not know the right notification channel or routing integration. **Context:** Those depend on observed retailer behavior and cost. **Evidence:** Neither SMS nor maps is in the frozen build. We would run a pilot, compare delivery completion and response times, then choose.
