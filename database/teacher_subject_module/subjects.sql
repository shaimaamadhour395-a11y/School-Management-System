


CREATE TABLE subjects (
    subject_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    description NVARCHAR(MAX),
    created_at DATETIME DEFAULT GETDATE()
);
INSERT INTO subjects (name, description)
VALUES 
('Math', 'Mathematics subject'),
('Science', 'Science subject');

SELECT * FROM subjects;

UPDATE subjects
SET description = 'Advanced Mathematics'
WHERE subject_id = 1;

DELETE FROM subjects
WHERE subject_id = 2;
