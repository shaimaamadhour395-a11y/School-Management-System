CREATE TABLE teachers (
    teacher_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100),
    phone NVARCHAR(20),
    created_at DATETIME DEFAULT GETDATE()
);
-- ≈÷«›… „⁄·„« 
INSERT INTO teachers (name, email, phone)
VALUES 
('Alaa Ahmed', 'alaa@example.com', '0123456789'),
('Sara Khaled', 'sara@example.com', '0987654321'),
('leen abd', 'abd@example.com', '0123456789');
SELECT * FROM teachers;


UPDATE teachers
SET phone = '0111222333'
WHERE teacher_id = 1;

DELETE FROM teachers
WHERE teacher_id = 2;






