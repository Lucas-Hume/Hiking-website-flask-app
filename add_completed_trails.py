"""
-----------------------
Inserts completed trails into trails.db. This is a one-time script to populate completed trails page.

Running from project root:
    python add_completed_trails.py

Able to be re-run — skips trails that already exist (matched by name + date).
"""

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "trails.db")

COMPLETED_TRAILS = [
    {
        "name":        "Dalpura Canyon",
        "lat":         -33.53299234223028,
        "lon":         150.3141848852404,
        "location":    "Bell, NSW",
        "date":        "2025-02-22",
        "difficulty":  "Hard",
        "distance_km": 5,
        "image_url":   "",
        "elevation":   223,
        "status":      "completed",
    },
]

def insert_trails(conn, trails):
    inserted = 0
    skipped  = 0

    for trail in trails:
        existing = conn.execute(
            "SELECT id FROM trails WHERE name = ? AND date = ?",
            (trail["name"], trail["date"])
        ).fetchone()

        if existing:
            print(f"  Skipped (already exists): {trail['name']} on {trail['date']}")
            skipped += 1
            continue

        conn.execute("""
            INSERT INTO trails
                (name, lat, lon, location, date, difficulty, distance_km, image_url, elevation, status)
            VALUES
                (:name, :lat, :lon, :location, :date, :difficulty, :distance_km, :image_url, :elevation, :status)
        """, trail)

        print(f"  Inserted: {trail['name']}")
        inserted += 1

    conn.commit()
    return inserted, skipped

def verify(conn):
    rows = conn.execute(
        "SELECT id, name, date, status, distance_km, elevation FROM trails"
    ).fetchall()
    print("\n-- Current trails in trails.db --")
    print(f"  {'ID':<4} {'Name':<25} {'Date':<12} {'Status':<10} {'Dist(km)':<10} {'Elev(m)'}")
    print("  " + "-" * 70)
    for row in rows:
        print(f"  {row[0]:<4} {row[1]:<25} {row[2]:<12} {row[3]:<10} {row[4]:<10} {row[5]}")
    print("------------------------\n")

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    try:
        inserted, skipped = insert_trails(conn, COMPLETED_TRAILS)
        verify(conn)
        print(f"Done.  {inserted} inserted, {skipped} skipped.")
    finally:
        conn.close()