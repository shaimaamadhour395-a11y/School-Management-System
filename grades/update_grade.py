import sqlite3

def update_grade():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    grade_id = int(input("Enter grade ID to update: "))
    new_grade = float(input("Enter new grade: "))

    cursor.execute(
        "UPDATE grades SET grade = ? WHERE id = ?",
        (new_grade, grade_id)
    )

    if cursor.rowcount == 0:
        print("No grade found with that ID.")
    else:
        print("Grade updated successfully!")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_grade()