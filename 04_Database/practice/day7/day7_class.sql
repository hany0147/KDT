SET autocommit = 0;

DROP TABLE users;
CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

START TRANSACTION;

INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;
-- ROLLBACK;
COMMIT;

DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);
SELECT * FROM articles;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', current_time(), current_time());

DELIMITER //
CREATE TRIGGER myTrigger
	BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = current_time();
END //
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id = 1;

CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAT DATETIME NOT NULL,
    PRIMARY KEY (id)
);
SELECT * FROM articleLogs;

DELIMITER //
CREATE TRIGGER trigLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogS (description, createdAt)
    VALUES ('글이 작성되었습니다.', current_time());
END//
DELIMITER ;

SHOW TRIGGERS;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title2', current_time(), current_time());

DROP TRIGGER trigLogs;

DELIMITER //
CREATE TRIGGER trigLogs
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogS (description, createdAt)
    VALUES (CONCAT(NEW.id, '번 글이 작성되었습니다.'), current_time());
END//
DELIMITER ;

INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title3', current_time(), current_time());

CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);
SELECT * FROM backupArticles;

DELIMITER //
CREATE TRIGGER backupTrigger
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

DELETE FROM articles
WHERE id = 1;