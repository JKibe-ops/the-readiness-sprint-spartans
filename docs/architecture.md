# Architecture and Data Model

## Chosen stack

- Python 3 + Flask: small HTTP surface, familiar routing, quick deployment.
- SQLite: zero infrastructure for the frozen prototype.
- Server-rendered HTML + CSS: fast first screen and minimal client complexity.
- JSON endpoint + 10-second browser polling: visible syncing without a queue or websocket service.

## Core flow

1. Retailer submits customer name, phone, address, item, and rider.
2. Server writes a delivery with status `Assigned`, timestamps, and rider.
3. Dispatcher sees all open requests on the board.
4. Rider advances status to `Picked Up`, then `Delivered`.
5. Scan confirmation sets the request to `Picked Up` in demo mode; production will validate a signed QR payload and record proof metadata.

## Data model

`deliveries(id, customer_name, phone, address, item_description, status, rider, created_at, updated_at)`

The prototype uses a constrained status vocabulary: Assigned, Picked Up, Delivered. Timestamps support sorting, sync freshness, and later audit history. A production version would add users, organizations, status_events, proof_of_delivery, and indexes on organization/status/updated_at.

## Outside the app

No SMS, payment, or map integration is included in the frozen build. These should be explicit adapters later, after operational metrics show which notification and routing gaps matter.
