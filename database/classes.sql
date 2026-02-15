-- database/classes.sql
CREATE TABLE IF NOT EXISTS classes (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    capacity   INTEGER CHECK (capacity >= 0),
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);