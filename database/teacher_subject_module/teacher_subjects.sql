DROP TABLE IF EXISTS teacher_subjects;

CREATE TABLE teacher_subjects (
    teacher_id INT,
    subject_id INT,
    PRIMARY KEY (teacher_id, subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
INSERT INTO teacher_subjects (teacher_id, subject_id)
VALUES 
(1, 1),
(1, 2);
SELECT t.name AS Teacher, s.name AS Subject
FROM teacher_subjects ts
JOIN teachers t ON ts.teacher_id = t.teacher_id
JOIN subjects s ON ts.subject_id = s.subject_id;

