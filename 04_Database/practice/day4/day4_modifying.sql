-- 문제 1
CREATE TABLE users(
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);
SHOW COLUMNS FROM users;
SELECT * FROM users;
DROP TABLE users;

-- 문제 2
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
    ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);
    
-- 문제 3
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Hui', 'Jang', '1993-01-01', 'Ansan', 'Korea', 'hany3@#@@bbb.kr'),
    ('Jua', 'Lee', '1993-03-31', 'Seoul', 'Korea', NULL),
    ('Dahee', 'Kim', '1945-04-09', 'Anyang', 'Korea', 'hhhhh@naver.com'),
    ('Kwangho', 'Jo', '1999-12-14', 'Mockpho', 'Korea', NULL);
-- 문제 4
UPDATE
	users
SET
	first_name = 'hanui',
    last_name = 'Jang',
    birthday = '1993-08-15'
WHERE
	userId = '2';
-- 문제 5
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country IS NULL;
-- 문제 6
DELETE FROM
	users
WHERE
	first_name = 'Beemo';
-- 문제 7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo'
    AND last_name = 'Lee';
-- 문제 8
DELETE FROM
	users
ORDER BY
	created_at DESC
LIMIT 1;