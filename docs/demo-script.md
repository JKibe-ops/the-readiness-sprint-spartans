# Demo Script (10 minutes)

**0:00–1:00 — Problem / John Kibe**
Explain that retailers coordinate through WhatsApp and calls, which hides ownership, status, and proof. Name the three roles.

**1:00–3:00 — Retailer intake / Joy**
Create a request for Brian Otieno, add a Nairobi address and item, assign Sasaki Benard. Point out the generated request ID and Assigned state.

**3:00–5:00 — Dispatcher board / Sasaki Benard**
Show all three seeded examples. Explain the single lifecycle and the counts. Use the action to move the new request to Picked Up.

**5:00–7:00 — Rider confirmation / Eunice Wanjiru**
Use the scan confirmation control. Explain that this is the reliable demo fallback and that production validates signed QR data. Move an active order to Delivered and point out POD VERIFIED.

**7:00–8:30 — Architecture / John Kibe**
Explain Flask, SQLite, server-rendered HTML, and the JSON polling endpoint. Mention why this is enough for the first operation.

**8:30–10:00 — Trade-offs and roadmap / Joy**
Name polling, SQLite, and demo scanning before the panel does. State the accepted reason and next upgrade for each. Close on reliability metrics: assignment time, completion rate, proof capture rate.

Keep the close focused on the delivery workflow and the measurable value of clearer handoffs.

## Handoffs

John owns problem and architecture. Joy owns intake and trade-offs. Sasaki owns dispatcher workflow. Eunice owns rider workflow and edge cases. Every presenter takes the first unscripted question in their area.

## Defense pattern

Answer in State → Context → Evidence order. Example: “We chose polling. The prototype is a single retailer workflow and polling keeps deployment simple. The browser calls `/api/deliveries` every 10 seconds and surfaces the last sync time.”
