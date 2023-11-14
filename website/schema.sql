DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS roles;

CREATE TABLE user(
    id INTEGER AUTO_INCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY (username)
);

CREATE TABLE roles(
    role_name TEXT NOT NULL CHECK (role_name IN ('admin', 'librarian', 'student')),
    username TEXT NOT NULL,
    FOREIGN KEY (username) REFERENCES user (username),
    PRIMARY KEY (username, role_name)
);