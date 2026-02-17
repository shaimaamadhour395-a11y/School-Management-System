from db import fetch_query

def show_grades_report():
    """
    Generates and prints a report of all grades with student and subject names.
    """
    try:
        query = """
        SELECT students.name AS student_name,
               subjects.name AS subject_name,
               grades.grade_value
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        ORDER BY students.name, subjects.name
        """
        results = fetch_query(query)

        print("===== Grades Report =====")
        if not results:
            print("No grades found.")
            return

        for row in results:
            print(f"Student: {row['student_name']} | Subject: {row['subject_name']} | Grade: {row['grade_value']}")
    except Exception as e:
        print("Error generating grades report:", e)