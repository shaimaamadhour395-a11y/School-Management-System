# attendance/add_attendance.py

from database.db import get_connection

def add_attendance(student_id, class_id, date, status, note=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO attendance
            (student_id, class_id, date, status, note)
            VALUES (?, ?, ?, ?, ?)
        """, (student_id, class_id, date, status, note))

        conn.commit()
        print("Attendance added successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    add_attendance(1, 2, "2026-02-17", "present", "on time")

                   
                     
