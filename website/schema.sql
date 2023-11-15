DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;

CREATE TABLE users(
    id INTEGER UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY (username)
);

CREATE TABLE roles(
    role_name TEXT NOT NULL CHECK (role_name IN ('admin', 'librarian', 'student')),
    username INTEGER NOT NULL,
    FOREIGN KEY (username) REFERENCES user (username),
    PRIMARY KEY (username, role_name)
);

-- CREATE TABLE needs_clearance(
--     username TEXT NOT NULL,

-- );