from db import fetch_query

def show_attendance_report():
    """
    Displays attendance summary for all students.
    """

    try:
        query = """
        SELECT 
            students.name,
            SUM(CASE WHEN attendance.status = 'Present' THEN 1 ELSE 0 END),
            SUM(CASE WHEN attendance.status = 'Absent' THEN 1 ELSE 0 END),
            SUM(CASE WHEN attendance.status = 'Late' THEN 1 ELSE 0 END)
        FROM attendance
        JOIN students ON attendance.student_id = students.id
        GROUP BY students.id
        """

        results = fetch_query(query)

        print("===== Attendance Summary Report =====")

        if not results:
            print("No attendance records found.")
            return

        for row in results:
            print(f"""
Student: {row[0]}
Present: {row[1]}
Absent: {row[2]}
Late: {row[3]}
---------------------------
""")

    except Exception as e:
        print("Error generating attendance report:", e)
