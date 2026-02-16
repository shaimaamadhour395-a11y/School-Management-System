# attendance/update_attendance.py

from database.db import get_connection

def update_attendance(attendance_id, status=None, note=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        fields = []
        values = []

        if status is not None:
            fields.append("status = ?")
            values.append(status)

        if note is not None:
            fields.append("note = ?")
            values.append(note)

        if not fields:
            print("No fields to update.")
            return

        values.append(attendance_id)

        query = f"""
            UPDATE attendance
            SET {", ".join(fields)}
            WHERE id = ?
        """

        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            print("No attendance record found with this ID.")
        else:
            print("Attendance updated successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    update_attendance(1, status="Late", note="Arrived 10 minutes late")
