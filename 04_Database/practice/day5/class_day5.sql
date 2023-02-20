CREATE TABLE users(
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);
-- DROP TABLE articles;
-- DROP TABLE users;

SHOW COLUMNS FROM users;
SHOW COLUMNS FROM articles;

SELECT * FROM users;
SELECT * FROM articles;

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);
    
SELECT
	articles.id, title, content, name
FROM
	articles
INNER JOIN users
	ON articles.userId = users.id;
    
SELECT
	products.productCode, products.productName, productlines.textDescription
FROM
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;

SELECT
	orders.orderNumber,
    orders.status,
    orderdetails.priceEach
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;

SELECT
	t1.orderNumber,
    status,
    SUM(priceEach * quantityOrdered) AS totalSales
FROM
	orders AS t1
INNER JOIN orderdetails AS t2
	ON t1.orderNumber = t2.orderNumber
GROUP BY
	t1.orderNumber;

SELECT
	t1.contactFirstName,
    t2.orderNumber,
    t2.status
FROM
	customers AS t1
LEFT JOIN orders AS t2
	ON t1.customerNumber = t2.customerNumber;
    
SELECT
	t1.contactFirstName,
    t2.orderNumber,
    t2.status
FROM
	customers AS t1
LEFT JOIN orders AS t2
	ON t1.customerNumber = t2.customerNumber
WHERE t2.orderNumber IS NULL;

SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON customers.salesRepEmployeeNumber = employees.employeeNumber; 

SELECT
	employeeNumber, firstName, customerNumber, contactFirstName
FROM
	customers
RIGHT JOIN employees
	ON customers.salesRepEmployeeNumber = employees.employeeNumber
WHERE customerNumber IS NULL;