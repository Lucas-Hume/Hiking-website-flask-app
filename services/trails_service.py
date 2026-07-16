import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "trails.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dicts instead of tuples
    return conn


def get_upcoming_trails():
    conn = get_db()
    try:
        rows = conn.execute(
            "SELECT * FROM trails WHERE status = ?", ("upcoming",)
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def get_completed_trails():
    conn = get_db()
    try:
        rows = conn.execute(
            "SELECT * FROM trails WHERE status = ?", ("completed",)
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()