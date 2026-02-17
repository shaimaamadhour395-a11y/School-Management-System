from db import fetch_query

def show_grades_report():
    """
    Displays grades report with student averages.
    """

    try:
        query = """
        SELECT 
            students.name,
            subjects.name,
            grades.grade_value
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        ORDER BY students.name
        """

        results = fetch_query(query)

        print("===== Grades Report =====")

        if not results:
            print("No grades found.")
            return

        current_student = None
        student_grades = []

        for row in results:
            student_name, subject_name, grade_value = row

            if current_student != student_name:
                if student_grades:
                    avg = sum(student_grades) / len(student_grades)
                    print(f"Average: {round(avg, 2)}")
                    print("=================================")

                current_student = student_name
                student_grades = []
                print(f"\nStudent: {student_name}")

            print(f"Subject: {subject_name} | Grade: {grade_value}")
            student_grades.append(grade_value)

        if student_grades:
            avg = sum(student_grades) / len(student_grades)
            print(f"Average: {round(avg, 2)}")

    except Exception as e:
        print("Error generating grades report:", e)
