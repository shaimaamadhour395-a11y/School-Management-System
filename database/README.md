# وحدة قاعدة البيانات الخاصة ب الطلاب :

This folder contains the database schema and SQL scripts related to the **Student Module**
of the School Management System.

## 📁 الملفات :
- `students.sql`  
  Contains the SQL code to create the `students` table and perform basic CRUD operations
  (Create, Read, Update, Delete).

## 🗄️ جداول / الطلاب :
The `students` table stores essential information about students.

### الاعمدة:
- `student_id` – Unique identifier for each student
- `first_name` – Student's first name
- `last_name` – Student's last name
- `date_of_birth` – Date of birth
- `gender` – Gender of the student
- `class_id` – Reference to the class the student belongs to
- `created_at` – Record creation timestamp

## ⚙️ الاستخدام
Run the `students.sql` file using your SQL database system (e.g., MySQL) to create the table
and test the provided queries.

