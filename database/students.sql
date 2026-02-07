-- ========================================
-- Student Management Module
-- Database Schema and Operations
-- ========================================

-- Table: students
-- Description: Stores basic information about students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female'),
    class_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student_class
        FOREIGN KEY (class_id)
        REFERENCES classes(class_id)
);
--إضافة طالب
INSERT INTO students (first_name, last_name, date_of_birth, gender, class_id)
VALUES ('Sara', 'Mohammad', '2011-03-15', 'Female', 1);

-- إضافة معلومات الطالب
UPDATE students
SET class_id = 2
WHERE student_id = 1;

-- حذف الطالب
DELETE FROM students
WHERE student_id = 1;

-- استرجاع الطلاب مع فصولهم
SELECT s.student_id,
       s.first_name,
       s.last_name,
       c.class_name
FROM students s
LEFT JOIN classes c
ON s.class_id = c.class_id;


-- End of Student Management Module
-- ========================================
