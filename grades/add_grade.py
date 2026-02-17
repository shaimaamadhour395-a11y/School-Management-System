from db import execute_query

def add_grade(student_id, subject_id, teacher_id, grade_value):
    """
    Adds a new grade record to the database.
    """
    try:
        query = """
        INSERT INTO grades (student_id, subject_id, teacher_id, grade_value)
        VALUES (?, ?, ?, ?)
        """
        execute_query(query, (student_id, subject_id, teacher_id, grade_value))
        print("Grade added successfully.")
    except Exception as e:
        print("Error adding grade:", e)