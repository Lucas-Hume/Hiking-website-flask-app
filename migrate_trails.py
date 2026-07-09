"""
migrate_trails.py
-----------------
One-time migration script: reads trails.json and inserts all records
into a SQLite database (trails.db).

Run from the project root:
    python migrate_trails.py

Safe to re-run — skips trails that already exist (matched by name + date).
"""

import json
import os
import sqlite3

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data", "trails.json")
DB_PATH   = os.path.join(BASE_DIR, "trails.db")

# ── Step 1: Create the database and trails table ──────────────────────────────
def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trails (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            lat           REAL    NOT NULL,
            lon           REAL    NOT NULL,
            location      TEXT,
            date          TEXT,
            difficulty    TEXT,
            distance_km   REAL,
            image_url     TEXT,
            elevation     REAL,
            status        TEXT    NOT NULL DEFAULT 'upcoming'
        )
    """)
    conn.commit()
    print("✔  Table ready.")

# ── Step 2: Load JSON ─────────────────────────────────────────────────────────
def load_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        trails = json.load(f)
    print(f"✔  Loaded {len(trails)} trail(s) from {JSON_PATH}")
    return trails

# ── Step 3: Insert records, skipping duplicates ───────────────────────────────
def migrate(conn, trails):
    inserted = 0
    skipped  = 0

    for trail in trails:
        # Check if this trail already exists (name + date combo)
        existing = conn.execute(
            "SELECT id FROM trails WHERE name = ? AND date = ?",
            (trail.get("name"), trail.get("date"))
        ).fetchone()

        if existing:
            print(f"  ↷  Skipped (already exists): {trail.get('name')} on {trail.get('date')}")
            skipped += 1
            continue

        conn.execute("""
            INSERT INTO trails
                (name, lat, lon, location, date, difficulty, distance_km, image_url, elevation, status)
            VALUES
                (:name, :lat, :lon, :location, :date, :difficulty, :distance_km, :image_url, :elevation, :status)
        """, {
            "name":        trail.get("name"),
            "lat":         trail.get("lat"),
            "lon":         trail.get("lon"),
            "location":    trail.get("location"),
            "date":        trail.get("date"),
            "difficulty":  trail.get("difficulty"),
            "distance_km": trail.get("distance_km"),
            "image_url":   trail.get("image_url"),
            "elevation":   trail.get("elevation"),
            "status":      trail.get("status", "upcoming"),  # default if missing
        })
        print(f"  ✔  Inserted: {trail.get('name')}")
        inserted += 1

    conn.commit()
    return inserted, skipped

# ── Step 4: Print a quick verification table ──────────────────────────────────
def verify(conn):
    rows = conn.execute(
        "SELECT id, name, date, status, distance_km, elevation FROM trails"
    ).fetchall()
    print("\n── Verification: rows now in trails.db ──────────────────────────")
    print(f"  {'ID':<4} {'Name':<20} {'Date':<12} {'Status':<10} {'Dist(km)':<10} {'Elev(m)'}")
    print("  " + "-" * 65)
    for row in rows:
        print(f"  {row[0]:<4} {row[1]:<20} {row[2]:<12} {row[3]:<10} {row[4]:<10} {row[5]}")
    print("─────────────────────────────────────────────────────────────────\n")

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nMigrating: {JSON_PATH}  →  {DB_PATH}\n")

    conn = sqlite3.connect(DB_PATH)

    try:
        init_db(conn)
        trails = load_json()
        inserted, skipped = migrate(conn, trails)
        verify(conn)
        print(f"Done.  {inserted} inserted, {skipped} skipped.")
    finally:
        conn.close()