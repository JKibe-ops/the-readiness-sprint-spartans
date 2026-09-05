# Reflex: The Readiness Sprint

A working Flask + SQLite prototype for small Kenyan retailers to log deliveries, assign riders, track status, and confirm handoff.

## Run the demo

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py app.py
```

Open http://127.0.0.1:5000. The seeded demo data represents a retailer, dispatcher, and rider handoff. Create a request, move it from Assigned to Picked Up to Delivered, and use the scan confirmation control.

## Team

John Kibe · Sasaki Benard · Joy · Eunice Wanjiru

## Deliverables

- [Executive narrative](docs/executive-narrative.md)
- [Architecture and data model](docs/architecture.md)
- [Trade-off log](docs/trade-off-log.md)
- [Demo script](docs/demo-script.md)
- [Timing log](docs/timing-log.md)
