# attendance/list_attendance.py

from database.db import get_connection

def list_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()

    for row in rows:
        print(dict(row))  

    conn.close()


if __name__ == "__main__":
    list_attendance()

  
