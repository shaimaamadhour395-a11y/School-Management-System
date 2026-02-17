import sqlite3

def list_grades():
    conn = sqlite3.connect("school.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.name AS student_name,
               subjects.name AS subject_name,
               grades.grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No grades found.")
    else:
        print("Grades Report:\n")
        for row in rows:
            print(f"{row['student_name']} - {row['subject_name']} : {row['grade']}")

    conn.close()

if __name__ == "__main__":
    list_grades()