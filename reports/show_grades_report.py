from database.db import fetch_query

def show_grades_report():
    """
    Displays grades report for all students.
    """

    try:
        query = """
        SELECT students.name, subjects.name, grades.grade_value
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        ORDER BY students.name
        """

        results = fetch_query(query)

        print("\n===== Grades Report =====\n")

        if not results:
            print("No grades found in the system.\n")
            return

        for row in results:
            student_name, subject_name, grade_value = row
            print(f"Student: {student_name}")
            print(f"Subject: {subject_name}")
            print(f"Grade: {grade_value}")
            print("------------------------")

    except Exception as e:
        print("Error generating grades report:", e)


if __name__ == "__main__":
    show_grades_report()
