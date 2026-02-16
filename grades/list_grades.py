from db import fetch_query

def list_grades():
    """
    Displays all grades with student and subject names.
    """

    try:
        query = """
        SELECT grades.id,
               students.name,
               subjects.name,
               grades.grade_value
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        """

        results = fetch_query(query)

        print("===== Grades List =====")

        if not results:
            print("No grades found.")
            return

        for row in results:
            print(f"ID: {row[0]} | Student: {row[1]} | Subject: {row[2]} | Grade: {row[3]}")

    except Exception as e:
        print("Error retrieving grades:", e)
