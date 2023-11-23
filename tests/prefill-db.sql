.mode json
.header on
.output ./tests/results.json
.open ./instance/website.sqlite

INSERT INTO users (first_name, last_name, username, password)
VALUES ('Jace', 'Merc', 'jace', 'scrypt:32768:8:1$KcXHqEQdawi2Nvwi$a6a76ec02ef514b0c24d60c23f762cb8a31eea358b09f4dfce128c957e8497852c69ca1d9204d7183793df6f6bdc5db539fa31201d0efcb710aff06991a7414d'),
       ('Sandy', 'Cheeks', 'sandy', 'scrypt:32768:8:1$qmlk9DuyqONqZJmj$1ae8e5a24dc83ff637e3ad0e8926a0b6e301c8c1863337df3f36b6ad609114fc52ef69833759a0d7809dc4f816b408b18d244695f71de3284ad605b3b5622581'),
       ('Admin', 'Guy', 'admin', 'scrypt:32768:8:1$Hn0ygRiNvBDoxU1m$ea2397f97cdd60c8580990c1c3f03e7b1ec9ecc25a153b039840e7fec166e31ffdfe3ad308f44c28ca351f175bdfd176aaa26199cf8ecf51b851d78341627984'),
       ('Patrick', 'Star', 'patrick', 'scrypt:32768:8:1$RmVJLo3EPjYTj3JW$45f6f5ff03c126698724abde306b0689a1b16a451a70b1a2dbe61cc303ae9f2fa1e885b73d5610b15b152e29c5c5ca07e2c9fc88a6c38cedeb84a3fb927c6342');

INSERT INTO roles (role_name, username, approval)
VALUES ('student', 'jace', 1),
       ('librarian', 'sandy', 0),
       ('admin', 'admin', 1),
       ('librarian', 'patrick', 1);

INSERT INTO books (isbn, title, author, quantity)
VALUES
    ('000-0-000-00000-1', 'Book 1', 'Author 1', 5),
    ('000-0-000-00000-2', 'Book 2', 'Author 2', 3),
    ('000-0-000-00000-3', 'Book 3', 'Author 3', 2),
    ('000-0-000-00000-4', 'Book 4', 'Author 4', 8),
    ('000-0-000-00000-5', 'Book 5', 'Author 5', 1),
    ('000-0-000-00000-6', 'Book 6', 'Author 6', 4),
    ('000-0-000-00000-7', 'Book 7', 'Author 7', 6),
    ('000-0-000-00000-8', 'Book 8', 'Author 8', 10),
    ('000-0-000-00000-9', 'Book 9', 'Author 9', 7),
    ('000-0-000-00000-0', 'Book 10', 'Author 10', 2),
    ('100-0-000-00000-1', 'Book 11', 'Author 11', 3),
    ('100-0-000-00000-2', 'Book 12', 'Author 12', 5),
    ('100-0-000-00000-3', 'Book 13', 'Author 13', 1),
    ('100-0-000-00000-4', 'Book 14', 'Author 14', 4),
    ('100-0-000-00000-5', 'Book 15', 'Author 15', 6),
    ('100-0-000-00000-6', 'Book 16', 'Author 16', 9),
    ('100-0-000-00000-7', 'Book 17', 'Author 17', 2),
    ('100-0-000-00000-8', 'Book 18', 'Author 18', 3),
    ('100-0-000-00000-9', 'Book 19', 'Author 19', 7),
    ('100-0-000-00000-0', 'Book 20', 'Author 20', 4);

INSERT INTO rooms (room_num) 
VALUES
    (101),
    (102),
    (103),
    (104),
    (105),
    (201),
    (202),
    (203),
    (204),
    (205),
    (301),
    (302),
    (303),
    (304),
    (305),
    (401),
    (402),
    (403),
    (404),
    (405);


SELECT * FROM users;
SELECT * FROM roles;
SELECT * FROM books;
SELECT * FROM rooms;