-- For: Create USERS table on the database hbtn_0d_tvshows
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);
