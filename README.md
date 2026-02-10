  # وحدة قاعدة البيانات الخاصة بالمعلمين والمواد

This folder contains the database schema and SQL scripts related to the **Teacher & Subject Module**  
of the School Management System.

## 📁 الملفات
- `teachers.sql`  
  Contains the SQL code to create the `teachers` table and perform basic CRUD operations.
- `subjects.sql`  
  Contains the SQL code to create the `subjects` table and perform basic CRUD operations.
- `teacher_subjects.sql`  
  Contains the SQL code to link teachers with subjects (`teacher_subjects` table).

## 🗄️ الجداول / المعلمات والمواد

### teachers
- `teacher_id` – Unique identifier for each teacher
- `first_name` – Teacher's first name
- `last_name` – Teacher's last name
- `email` – Teacher's email
- `created_at` – Record creation timestamp

### subjects
- `subject_id` – Unique identifier for each subject
- `subject_name` – Name of the subject
- `created_at` – Record creation timestamp

### teacher_subjects
- `id` – Unique identifier
- `teacher_id` – Reference to a teacher
- `subject_id` – Reference to a subject

## ⚙️ الاستخدام
Run the `.sql` files using your SQL database system (e.g., MySQL, SQL Server)  
to create the tables and test the provided queries.
