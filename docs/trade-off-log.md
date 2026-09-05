# One-Page Trade-off Log

## 1. SQLite instead of Postgres
**Weak point:** SQLite is a single-file database and is not the right choice for many concurrent retailers.

**Acceptable because:** The prototype has one operating loop, no infrastructure requirement, and a tiny dataset. A local database makes the demo reproducible and the data model easy to defend.

**With more time:** Move to Postgres, add organization IDs, indexes, migrations, backups, and connection pooling. Load-test concurrent assignments.

## 2. Polling instead of real-time push
**Weak point:** A 10-second poll can be stale and creates repeated requests.

**Acceptable because:** It is transparent, robust on basic hosting, and enough to demonstrate syncing without introducing websocket operations before the core workflow is validated.

**With more time:** Use server-sent events or WebSockets, reconnect logic, and a small event/outbox table. Measure freshness p95 and request volume.

## 3. Scan confirmation has a demo fallback
**Weak point:** The current scan control demonstrates the rider action but does not decode or cryptographically validate a QR code.

**Acceptable because:** The case asks us to support scanning for order confirmation, and the frozen build needs a reliable presentation path even without camera permissions or generated labels.

**With more time:** Generate signed per-order QR payloads, decode with a browser library, reject mismatched/expired payloads, and attach photo/GPS/time proof.

## 4. One status row instead of an event history
**Weak point:** Updating the status overwrites the previous state, so the prototype cannot answer who changed it or reconstruct a timeline.

**Acceptable because:** The MVP question is visibility of the current delivery state; it keeps the first data model small.

**With more time:** Add append-only status events, actor identity, idempotency keys, and a delivery timeline UI.
