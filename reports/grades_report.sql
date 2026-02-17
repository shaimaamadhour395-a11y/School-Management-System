SELECT 
    students.name AS student_name,
    subjects.name AS subject_name,
    grades.grade_value,
    AVG(grades.grade_value) OVER (PARTITION BY students.id) AS student_average
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id;
