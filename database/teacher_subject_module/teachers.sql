CREATE TABLE teachers (
    teacher_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100),
    phone NVARCHAR(20),
    created_at DATETIME DEFAULT GETDATE()
);
