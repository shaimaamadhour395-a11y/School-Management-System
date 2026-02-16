-- database/grades.sql
CREATE TABLE IF NOT EXISTS grades (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id  INTEGER NOT NULL,
    subject_id  INTEGER NOT NULL,
    term        TEXT    NOT NULL, -- مثال: 'Term 1' أو '2025-T1'
    grade       REAL    NOT NULL CHECK (grade >= 0),
    note        TEXT,
    created_at  TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE (student_id, subject_id, term),
    FOREIGN KEY (student_id) REFERENCES students(id)  ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_grades_student_subject ON grades(student_id, subject_id);
CREATE INDEX IF NOT EXISTS idx_grades_term            ON grades(term);