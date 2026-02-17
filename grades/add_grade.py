import sqlite3

def add_grade():
    conn = sqlite3.connect("school.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    student_id = int(input("Enter student ID: "))
    subject_id = int(input("Enter subject ID: "))
    grade = float(input("Enter grade: "))

    cursor.execute(
        "INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
        (student_id, subject_id, grade)
    )

    conn.commit()
    conn.close()

    print("Grade added successfully!")

if __name__ == "__main__":
    add_grade()