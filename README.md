# Mini School Management System (Mini SMS)

## الهدف
نظام مصغر لكنه واقعي ومتكامل لإدارة:
- الطلاب
- المعلمين
- المواد
- الصفوف
- الحضور
- الدرجات

---

## 👨‍💻 الطالب 1: Student Management Module
(وحدة إدارة الطلاب)

### ما ينفذه فعليًا:
- إضافة طالب (`INSERT students`)
- تعديل بيانات طالب (`UPDATE students`)
- حذف طالب (`DELETE students`)
- عرض قائمة الطلاب (`SELECT students`)
- ربط الطالب بالصف (`students.class_id`)

### قاعدة البيانات:
- جدول: `students`
- علاقة: مع جدول `classes`

### Git / Jira:
- Branch: `feature/student-module`
- Commits باسمه
- Tasks في Jira خاصة بالطلاب

### الملفات:
- `database/README.md`
- `database/students.sql`

---

## 👨‍💻 الطالب 2: Teacher & Subject Module
(إدارة المعلمين والمواد)

### ما ينفذه فعليًا:
- إضافة معلم (`teachers`)
- إضافة مادة (`subjects`)
- ربط المعلم بالمادة (`teacher_subjects`)
- عرض المواد والمعلمين

### قاعدة البيانات:
- الجداول: `teachers`, `subjects`, `teacher_subjects`

### Git / Jira:
- Branch: `feature/teacher-subject-module`
- Commits مستقلة
- Tasks موثقة في Jira

### الملفات:
- `database/teacher_subject_module/teachers.sql`
- `database/teacher_subject_module/subjects.sql`
- `database/teacher_subject_module/teacher_subjects.sql`

---

## 📁 تفاصيل قاعدة بيانات Teacher & Subject Module

This folder contains the database schema and SQL scripts related to the Teacher & Subject Module.

### الملفات

- `teachers.sql`  
  Contains the SQL code to create the teachers table and perform basic CRUD operations.

- `subjects.sql`  
  Contains the SQL code to create the subjects table and perform basic CRUD operations.

- `teacher_subjects.sql`  
  Contains the SQL code to link teachers with subjects.

### الجداول

#### teachers
- teacher_id – Unique identifier for each teacher
- first_name – Teacher's first name
- last_name – Teacher's last name
- email – Teacher's email
- created_at – Record creation timestamp

#### subjects
- subject_id – Unique identifier for each subject
- subject_name – Name of the subject
- created_at – Record creation timestamp

#### teacher_subjects
- id – Unique identifier
- teacher_id – Reference to teachers table
- subject_id – Reference to subjects table

---

## 👨‍💻 الطالب 3: Class, Attendance & Grades Module
(الصفوف، الحضور، الدرجات)

### ما ينفذه فعليًا:
- إنشاء صف (`classes`)
- تسجيل حضور طالب (`attendance`)
- إدخال درجات (`grades`)
- عرض تقارير (Grades / Attendance)

### قاعدة البيانات:
- الجداول: `classes`, `attendance`, `grades`

### الملفات:

attendance/
- add_attendance.py
- delete_attendance.py
- list_attendance.py
- update_attendance.py

classes/
- add_class.py
- delete_class.py
- list_classes.py
- update_class.py

grades/
- add_grade.py
- delete_gardes.py
- list_grades.py
- update_grade.py

reports/
- attendance_summary.sql
- grades_report.sql
- show_attendance_report.py
- show_grades_report.py

database/
- attendance.sql
- classes.sql
- grades.sql
- subjects.sql
- db.py

---

## 👨‍💻 الطالب 4: Integration, UI & Documentation

### ما ينفذه فعليًا:
- دمج جميع Modules
- واجهة بسيطة
- كتابة README النهائي
- توثيق المشروع
- ER Diagram
- Screenshots من GitHub و Jira

---

## طريقة تشغيل المشروع

1. افتح نظام إدارة قواعد البيانات مثل MySQL أو SQL Server
2. شغل ملفات SQL بالترتيب:

students.sql  
teachers.sql  
subjects.sql  
teacher_subjects.sql  
classes.sql  
attendance.sql  
grades.sql  

3. تأكد من إنشاء الجداول بنجاح

4. شغل سكربتات Python من المجلدات:

attendance  
classes  
grades  
reports  

---

## Repository

جميع ملفات المشروع موجودة في GitHub Repository.

---



## 📸 Screenshots

### 📊 Grades Report
![Grades Report](screenshots/grades_report.png)

---

### 📅 Attendance Report
![Attendance Report](screenshots/attendance_report.png)

---

### 🗄 Database Tables
![Database Tables](screenshots/database_tables.png)

