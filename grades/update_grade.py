from db import execute_query

def update_grade(grade_id, new_grade_value):
    """
    Updates the value of an existing grade.
    """

    try:
        query = """
        UPDATE grades
        SET grade_value = ?
        WHERE id = ?
        """
        execute_query(query, (new_grade_value, grade_id))
        print("Grade updated successfully.")

    except Exception as e:
        print("Error updating grade:", e)
