from datetime import datetime
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "reflex.db"
app = Flask(__name__)

STATUSES = ["Assigned", "Picked Up", "Delivered"]
RIDERS = ["Rider 01", "Rider 02", "Rider 03"]


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()
    connection.execute(
        """CREATE TABLE IF NOT EXISTS deliveries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            item_description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Assigned',
            rider TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            confirmation_at TEXT
        )"""
    )
    columns = {row[1] for row in connection.execute("PRAGMA table_info(deliveries)").fetchall()}
    if "confirmation_at" not in columns:
        connection.execute("ALTER TABLE deliveries ADD COLUMN confirmation_at TEXT")
    connection.execute("UPDATE deliveries SET rider = 'Rider 01' WHERE rider NOT IN ('Rider 01', 'Rider 02', 'Rider 03')")
    count = connection.execute("SELECT COUNT(*) FROM deliveries").fetchone()[0]
    if count == 0:
        now = datetime.now().isoformat(timespec="seconds")
        connection.executemany(
            """INSERT INTO deliveries
            (customer_name, phone, address, item_description, status, rider, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            [
                ("Amina Wekesa", "+254 712 440 118", "Kilimani, Nairobi", "Bluetooth speaker", "Picked Up", "Rider 01", now, now),
                ("Peter Mwangi", "+254 722 908 331", "Westlands, Nairobi", "Router and ethernet cable", "Assigned", "Rider 02", now, now),
                ("Faith Njeri", "+254 701 552 670", "South B, Nairobi", "Pharmacy refill pack", "Delivered", "Rider 03", now, now),
            ],
        )
    connection.commit()
    connection.close()


def serialize(row):
    item = dict(row)
    item["created_label"] = item["created_at"].replace("T", " ")
    return item


@app.route("/")
def dashboard():
    connection = get_db()
    deliveries = [serialize(row) for row in connection.execute("SELECT * FROM deliveries ORDER BY updated_at DESC").fetchall()]
    connection.close()
    counts = {status: sum(delivery["status"] == status for delivery in deliveries) for status in STATUSES}
    confirmed_id = request.args.get("confirmed", type=int)
    return render_template(
        "index.html",
        deliveries=deliveries,
        counts=counts,
        riders=RIDERS,
        confirmed_id=confirmed_id,
    )


@app.post("/deliveries")
def create_delivery():
    fields = ["customer_name", "phone", "address", "item_description"]
    values = [request.form.get(field, "").strip() for field in fields]
    if all(values):
        now = datetime.now().isoformat(timespec="seconds")
        connection = get_db()
        connection.execute(
            """INSERT INTO deliveries
            (customer_name, phone, address, item_description, status, rider, created_at, updated_at)
            VALUES (?, ?, ?, ?, 'Assigned', ?, ?, ?)""",
            (*values, request.form.get("rider") or "Rider 01", now, now),
        )
        connection.commit()
        connection.close()
    return redirect(url_for("dashboard"))


@app.post("/deliveries/<int:delivery_id>/status")
def update_status(delivery_id):
    status = request.form.get("status")
    rider = request.form.get("rider")
    if status in STATUSES:
        connection = get_db()
        connection.execute(
            "UPDATE deliveries SET status = ?, rider = COALESCE(?, rider), updated_at = ? WHERE id = ?",
            (status, rider, datetime.now().isoformat(timespec="seconds"), delivery_id),
        )
        connection.commit()
        connection.close()
    return redirect(url_for("dashboard"))


@app.get("/api/deliveries")
def deliveries_api():
    connection = get_db()
    rows = [serialize(row) for row in connection.execute("SELECT * FROM deliveries ORDER BY updated_at DESC").fetchall()]
    connection.close()
    return jsonify(rows)


@app.post("/deliveries/<int:delivery_id>/scan")
def scan_delivery(delivery_id):
    confirmed_at = datetime.now().isoformat(timespec="seconds")
    connection = get_db()
    connection.execute(
        "UPDATE deliveries SET status = 'Picked Up', confirmation_at = ?, updated_at = ? WHERE id = ?",
        (confirmed_at, confirmed_at, delivery_id),
    )
    connection.commit()
    connection.close()
    return redirect(url_for("dashboard", confirmed=delivery_id))


init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
