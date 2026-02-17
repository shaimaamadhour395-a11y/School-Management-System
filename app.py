from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# ===== تهيئة التطبيق =====
app = Flask(__name__, template_folder="ui")

# ===== قاعدة البيانات =====
def connect_db():
    conn = sqlite3.connect("school.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# ===== الصفحة الرئيسية =====
@app.route("/")
def home():
    return render_template("index.html")

# ==================== الطلاب ====================
@app.route("/students")
def students():
    conn = connect_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    classes = conn.execute("SELECT * FROM classes").fetchall()
    conn.close()
    return render_template("students.html", students=students, classes=classes)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    conn = connect_db()
    if request.method == "POST":
        name = request.form["name"]
        class_id = request.form["class_id"]
        conn.execute("INSERT INTO students (name, class_id) VALUES (?, ?)", (name, class_id))
        conn.commit()
        conn.close()
        return redirect(url_for("students"))
    classes = conn.execute("SELECT * FROM classes").fetchall()
    conn.close()
    return render_template("edit_student.html", student={"id": 0}, classes=classes)

@app.route("/edit_student/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    conn = connect_db()
    if request.method == "POST":
        name = request.form["name"]
        class_id = request.form["class_id"]
        conn.execute("UPDATE students SET name=?, class_id=? WHERE id=?", (name, class_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for("students"))
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    classes = conn.execute("SELECT * FROM classes").fetchall()
    conn.close()
    return render_template("edit_student.html", student=student, classes=classes)

@app.route("/delete_student/<int:id>")
def delete_student(id):
    conn = connect_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("students"))

# ==================== المعلمين ====================
@app.route("/teachers")
def teachers():
    conn = connect_db()
    teachers = conn.execute("SELECT * FROM teachers").fetchall()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()
    return render_template("teachers.html", teachers=teachers, subjects=subjects)

@app.route("/add_teacher", methods=["POST"])
def add_teacher():
    name = request.form["name"]
    conn = connect_db()
    conn.execute("INSERT INTO teachers (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for("teachers"))

@app.route("/edit_teacher/<int:id>", methods=["GET", "POST"])
def edit_teacher(id):
    conn = connect_db()
    if request.method == "POST":
        name = request.form["name"]
        conn.execute("UPDATE teachers SET name=? WHERE id=?", (name, id))
        conn.commit()
        conn.close()
        return redirect(url_for("teachers"))
    teacher = conn.execute("SELECT * FROM teachers WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit_teacher.html", teacher=teacher)

@app.route("/delete_teacher/<int:id>")
def delete_teacher(id):
    conn = connect_db()
    conn.execute("DELETE FROM teachers WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("teachers"))

# ==================== المواد ====================
@app.route("/subjects")
def subjects():
    conn = connect_db()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()
    return render_template("subjects.html", subjects=subjects)

@app.route("/add_subject", methods=["POST"])
def add_subject():
    name = request.form["name"]
    conn = connect_db()
    conn.execute("INSERT INTO subjects (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for("subjects"))

@app.route("/edit_subject/<int:id>", methods=["GET", "POST"])
def edit_subject(id):
    conn = connect_db()
    if request.method == "POST":
        name = request.form["name"]
        conn.execute("UPDATE subjects SET name=? WHERE id=?", (name, id))
        conn.commit()
        conn.close()
        return redirect(url_for("subjects"))
    subject = conn.execute("SELECT * FROM subjects WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit_subject.html", subject=subject)

@app.route("/delete_subject/<int:id>")
def delete_subject(id):
    conn = connect_db()
    conn.execute("DELETE FROM subjects WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("subjects"))

# ==================== الدرجات ====================
@app.route("/grades")
def grades():
    conn = connect_db()
    grades = conn.execute("""
        SELECT grades.id, students.name AS student, subjects.name AS subject, grades.grade, grades.student_id, grades.subject_id
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
    """).fetchall()
    students = conn.execute("SELECT * FROM students").fetchall()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()
    return render_template("grades.html", grades=grades, students=students, subjects=subjects)

@app.route("/add_grade", methods=["POST"])
def add_grade():
    student_id = request.form["student_id"]
    subject_id = request.form["subject_id"]
    grade = request.form["grade"]
    conn = connect_db()
    conn.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)", (student_id, subject_id, grade))
    conn.commit()
    conn.close()
    return redirect(url_for("grades"))

@app.route("/edit_grade/<int:id>", methods=["GET", "POST"])
def edit_grade(id):
    conn = connect_db()
    if request.method == "POST":
        student_id = request.form["student_id"]
        subject_id = request.form["subject_id"]
        grade_val = request.form["grade"]
        conn.execute("UPDATE grades SET student_id=?, subject_id=?, grade=? WHERE id=?", (student_id, subject_id, grade_val, id))
        conn.commit()
        conn.close()
        return redirect(url_for("grades"))
    grade = conn.execute("SELECT * FROM grades WHERE id=?", (id,)).fetchone()
    students = conn.execute("SELECT * FROM students").fetchall()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()
    return render_template("edit_grade.html", grade=grade, students=students, subjects=subjects)

@app.route("/delete_grade/<int:id>")
def delete_grade(id):
    conn = connect_db()
    conn.execute("DELETE FROM grades WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("grades"))

# ==================== الحضور ====================
@app.route("/attendance")
def attendance():
    conn = connect_db()
    attendance = conn.execute("""
        SELECT attendance.id, students.name AS student, attendance.status, attendance.date
        FROM attendance
        JOIN students ON attendance.student_id = students.id
    """).fetchall()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("attendance.html", attendance=attendance, students=students)

@app.route("/add_attendance", methods=["POST"])
def add_attendance():
    student_id = request.form["student_id"]
    status = request.form["status"]
    date = request.form["date"]
    conn = connect_db()
    conn.execute("INSERT INTO attendance (student_id, status, date) VALUES (?, ?, ?)", (student_id, status, date))
    conn.commit()
    conn.close()
    return redirect(url_for("attendance"))

@app.route("/edit_attendance/<int:id>", methods=["GET", "POST"])
def edit_attendance(id):
    conn = connect_db()
    if request.method == "POST":
        student_id = request.form["student_id"]
        status = request.form["status"]
        date = request.form["date"]
        conn.execute("UPDATE attendance SET student_id=?, status=?, date=? WHERE id=?", (student_id, status, date, id))
        conn.commit()
        conn.close()
        return redirect(url_for("attendance"))
    att = conn.execute("SELECT * FROM attendance WHERE id=?", (id,)).fetchone()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("edit_attendance.html", attendance=att, students=students)

@app.route("/delete_attendance/<int:id>")
def delete_attendance(id):
    conn = connect_db()
    conn.execute("DELETE FROM attendance WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("attendance"))

# ===== تشغيل السيرفر =====
if __name__ == "__main__":
    app.run(debug=True)