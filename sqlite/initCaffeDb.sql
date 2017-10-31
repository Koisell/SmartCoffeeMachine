DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,intensity INTEGER, volume INTEGER);
INSERT INTO User (username,intensity,volume) VALUES ('Romain','3','3');
