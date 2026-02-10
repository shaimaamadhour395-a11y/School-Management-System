# Classes, Attendance, and Grades Module
### Aya abd ullatif – School Management System

This README describes all the work done in the **Classes, Attendance, and Grades** module, including database structure, responsibilities, and code files.

---

## 📘 Module Responsibilities
This module is responsible for:
- Managing **Classes** (Add, Update, Delete, List)
- Recording **Attendance** for students
- Managing **Grades** for students and subjects

---

## 📂 Project Folder Structure

```
classes/
    add_class.py
    update_class.py
    delete_class.py
    list_classes.py

attendance/
    add_attendance.py
    list_attendance.py

grades/
    add_grade.py
    list_grades.py

database/
    classes.sql
    attendance.sql
    grades.sql
```

---

## 🧱 Database Tables (Created by Aya abd ullatif)

### 🏫 `classes` Table
Stores information about each class.

| Column      | Type          | Description                |
|-------------|---------------|----------------------------|
| id          | INTEGER (PK)  | Class unique identifier    |
| name        | TEXT          | Class title/name           |
| capacity    | INTEGER       | Maximum number of students |
| created_at  | TIMESTAMP     | Creation time              |

---

### 📅 `attendance` Table
Tracks student attendance per day.

| Column      | Type          | Description                      |
|-------------|---------------|----------------------------------|
| id          | INTEGER (PK)  | Record ID                        |
| student_id  | INTEGER (FK)  | Reference to students table      |
| class_id    | INTEGER (FK)  | Reference to classes table       |
| date        | DATE          | Attendance date                  |
| status      | TEXT          | Present / Absent / Late          |

---

### 📝 `grades` Table
Stores student grades for each subject.

| Column      | Type          | Description                      |
|-------------|---------------|----------------------------------|
| id          | INTEGER (PK)  | Record ID                        |
| student_id  | INTEGER (FK)  | Reference to students table      |
| subject_id  | INTEGER (FK)  | Reference to subjects table      |
| term        | TEXT          | Academic term (e.g., Term 1)     |
| grade       | REAL          | Score                            |

---

## 🧪 SQL Scripts
All SQL scripts related to this module are stored inside:
```
database/classes.sql  
database/attendance.sql  
database/grades.sql
```

Each script contains:
- Table creation  
- Example INSERT commands  
- Example SELECT commands  

---

## 🧩 Python Code (If applicable)
All module functions are stored inside:
```
classes/
attendance/
grades/
```

Each file handles a specific operation such as **add**, **update**, **delete**, or **list**.

---

## ✔️ Conclusion
This README summarizes all work completed in the third module of the School Management System. All created tables, code files, and responsibilities are documented clearly for grading and review.