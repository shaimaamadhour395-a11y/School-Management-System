from db import execute_query

def delete_grade(grade_id):
    """
    Deletes a grade from the database.
    """
    try:
        query = "DELETE FROM grades WHERE id = ?"
        execute_query(query, (grade_id,))
        print("Grade deleted successfully.")
    except Exception as e:
        print("Error deleting grade:", e)