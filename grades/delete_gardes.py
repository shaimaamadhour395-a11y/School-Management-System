import sqlite3

def delete_grade():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    grade_id = int(input("Enter grade ID to delete: "))

    cursor.execute(
        "DELETE FROM grades WHERE id = ?",
        (grade_id,)
    )

    if cursor.rowcount == 0:
        print("No grade found with that ID.")
    else:
        print("Grade deleted successfully!")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_grade()