# Executive Narrative: Reflex

**Team:** John Kibe, Sasaki Benard, Joy, Eunice Wanjiru

## Slide 1 — Problem
**Takeaway:** WhatsApp coordination hides delivery ownership and proof.

Small retailers currently coordinate deliveries through chats and calls. That means no reliable assignment record, no shared status, and no proof of delivery when a customer asks what happened.

## Slide 2 — Solution
**Takeaway:** Reflex gives every request one visible lifecycle.

A retailer logs the customer and item, a dispatcher assigns a rider, and the rider moves the request through Assigned → Picked Up → Delivered. Scanning supports order confirmation at handoff.

## Slide 3 — Architecture
**Takeaway:** A small relational core is enough for the first operating loop.

Flask serves the web interface and JSON sync endpoint. SQLite stores deliveries with a single status and timestamps. The browser polls for fresh requests. This keeps the system easy to deploy and explain while proving the workflow.

## Slide 4 — Trade-offs
**Takeaway:** We optimized for a demonstrable, trustworthy workflow over scale.

We accepted polling, SQLite, and a demo scan fallback because the case study is one retailer operation. Each has a clear upgrade path documented in the trade-off log.

## Slide 5 — Roadmap
**Takeaway:** The next milestone is operational reliability, not more screens.

Add authentication and role permissions, offline-first rider updates, real QR validation, Postgres, and event-driven notifications. Measure assignment time, delivery completion rate, and proof capture rate before expanding scope.
