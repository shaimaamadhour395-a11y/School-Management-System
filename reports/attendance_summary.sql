SELECT 
    students.name AS student_name,
    SUM(CASE WHEN attendance.status = 'Present' THEN 1 ELSE 0 END) AS total_present,
    SUM(CASE WHEN attendance.status = 'Absent' THEN 1 ELSE 0 END) AS total_absent,
    SUM(CASE WHEN attendance.status = 'Late' THEN 1 ELSE 0 END) AS total_late
FROM attendance
JOIN students ON attendance.student_id = students.id
GROUP BY students.id;
