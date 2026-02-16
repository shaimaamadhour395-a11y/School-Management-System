# attendance/delete_attendance.py

from database.db import get_connection

def delete_attendance(attendance_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM attendance WHERE id = ?",
            (attendance_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            print("No attendance record found with this ID.")
        else:
            print("Attendance deleted successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    delete_attendance(1)


  

