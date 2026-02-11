
# Mini School Management System (Mini SMS)
#الهدف:
نظام مصغر لكنه واقعي ومتكامل لإدارة:
- الطلاب
- المعلمين
- المواد
- الصفوف
- الحضور
- الدرجات

---

## 👨‍لالب 1: Student Management Module
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

## 👨‍💻 الطالب 3: Class, Attendance & Grades Module
(الصفوف، الحضور، الدرجات)

### ما ينفذه فعليًا:
- إنشاء صف (`classes`)
- تسجيل حضور طالب (`attendance`)
- إدخال درجات (`grades`)
- عرض تقارير (Grades / Attendance)

### قاعدة البيانات:
- الجداول: `classes`, `attendance`, `grades`

### Git / Jira:
- Branch: `feature/class-attendance-grades`
- Commits واضحة
- Jira Tasks منفصلة

### الملفات:
- `attendance/`  
  - `add_attendance.py`, `delete_attendance.py`, `list_attendance.py`, `update_attendance.py`
- `classes/`  
  - `add_class.py`, `delete_class.py`, `list_classes.py`, `update_class.py`
- `grades/`  
  - `add_grade.py`, `delete_gardes.py`, `list_grades.py`, `update_grade.py`
- `reports/`  
  - `attendance_summary.sql`, `grades_report.sql`, `show_attendance_report.py`, `show_grades_report.py`
- `database/`  
  - `attendance.sql`, `classes.sql`, `grades.sql`, `subjects.sql`, `db.py`, `README.md`
- `sms.db`

---

## 👨‍💻 الطالب 4: Integration, UI & Documentation
(الدمج، الواجهة، التوثيق)

### ما ينفذه فعليًا:
- دمج جميع الـ Modules
- واجهة: CLI أو Web بسيطة
- كتابة README.md نهائي
- توثيق النظام:
  - Screenshots من Jira و GitHub
  - ER Diagram لقواعد البيانات

### Git / Jira:
- Branch: `feature/ui-docs`
- Pull Requests
- Documentation كاملة

---

## **استخدام المشروع**
1. افتح أي نظام إدارة قواعد بيانات (MySQL, SQL Server أو أي DBMS مناسب).
2. شغّل ملفات `.sql` حسب ترتيب الجداول:
   - `students.sql` → `teachers.sql` → `subjects.sql` → `teacher_subjects.sql` → `classes.sql` → `attendance.sql` → `grades.sql`
3. تأكد من الربط الصحيح بين الجداول عند الاختبارات.
4. كل ملفات المشروع موجودة على GitHub ضمن البرانش `feature/integration-ui-docs`.
5. يمكن تشغيل السكريبتات Python حسب المجلدات لتجربة إضافة/تعديل/حذف/عرض البيانات.

---

## 🔹 ملاحظات عامة
- كل Module مستقل لكنه مدموج على نفس البرانش النهائي.
- README هذا يمثل **توثيق كامل لكل الطلاب الثلاث + دمج العمل النهائي للواجهة والتوثيق**.
- يمكن للدكتور مراجعة كل الملفات، الجداول، والـ ER Diagram من هنا.
>>>>>>> 0ac5864 (Add final README with all students' modules)
