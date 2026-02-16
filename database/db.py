# database/db.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "sms.db"  # قاعدة البيانات بالروت

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    # تفعيل العلاقات الخارجية في SQLite ضروري لقيود FK
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn