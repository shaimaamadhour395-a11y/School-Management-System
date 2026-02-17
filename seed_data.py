import sqlite3

def seed():
    conn = sqlite3.connect("school.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # Insert Classes
    cursor.execute("INSERT INTO classes (name, description) VALUES (?, ?)",
                   ("Grade 10", "Tenth Grade"))
    cursor.execute("INSERT INTO classes (name, description) VALUES (?, ?)",
                   ("Grade 11", "Eleventh Grade"))

    # Insert Subjects
    cursor.execute("INSERT INTO subjects (name) VALUES (?)", ("Mathematics",))
    cursor.execute("INSERT INTO subjects (name) VALUES (?)", ("Physics",))

    # Get IDs
    class_id = cursor.execute("SELECT id FROM classes WHERE name='Grade 10'").fetchone()[0]
    math_id = cursor.execute("SELECT id FROM subjects WHERE name='Mathematics'").fetchone()[0]
    physics_id = cursor.execute("SELECT id FROM subjects WHERE name='Physics'").fetchone()[0]

    # Insert Students
    cursor.execute("INSERT INTO students (name, age, gender, class_id) VALUES (?, ?, ?, ?)",
                   ("Ahmad", 16, "Male", class_id))
    cursor.execute("INSERT INTO students (name, age, gender, class_id) VALUES (?, ?, ?, ?)",
                   ("Sara", 15, "Female", class_id))

    # Get Student IDs
    ahmad_id = cursor.execute("SELECT id FROM students WHERE name='Ahmad'").fetchone()[0]
    sara_id = cursor.execute("SELECT id FROM students WHERE name='Sara'").fetchone()[0]

    # Insert Grades
    cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                   (ahmad_id, math_id, 95))
    cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                   (sara_id, physics_id, 88))

    # Insert Attendance
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                   (ahmad_id, "2026-02-17", "Present"))
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                   (sara_id, "2026-02-17", "Absent"))

    conn.commit()
    conn.close()

    print("Sample data inserted successfully!")

if __name__ == "__main__":
    seed()