-- 문제 1
SELECT * FROM products;
SELECT
	productCode, productName, MSRP
FROM
	products
WHERE MSRP > (SELECT AVG(MSRP) FROM products)
ORDER BY MSRP;

-- 문제 2
SELECT * FROM orders;
SELECT
	customerNumber, customerName, t1.orderDate
FROM (
	SELECT
		*
    FROM
		customers
	INNER JOIN orders USING (customerNumber)
) AS t1
WHERE '2003-01-06' <= t1.orderDate 
		AND t1.orderDate <= '2003-03-26'
ORDER BY customerNumber;

-- 문제 3-1
SELECT * FROM products;
SELECT productCode, productName, productLine, MSRP
FROM (
	SELECT
		*
	FROM 
		products
	WHERE
		productLine = 'Classic Cars'
) AS t1
ORDER BY t1.MSRP DESC
LIMIT 1;

-- 문제 3-2
SELECT productCode, productName, productLine, MSRP
FROM (
	SELECT
		*
	FROM 
		products
	WHERE
		productLine = 'Classic Cars'
) AS t1
WHERE MSRP = (SELECT MAX(MSRP) FROM products);
-- Error Code: 1146. Table 'classicmodels.t3' doesn't exist

-- 문제 4-1
SELECT * FROM customers;
SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE country = (
	SELECT country
    FROM customers
    GROUP BY country
    ORDER BY count(country) DESC
    LIMIT 1
)
ORDER BY customerNumber;
-- 문제 4-2
SELECT
	customerNumber, customerName, country
FROM
	customers
WHERE country = (
	SELECT MAX(country)
    FROM customers
)
ORDER BY customerNumber;

-- 문제 5-1
SELECT * FROM customers;
SELECT * FROM orders;

SELECT
	customerNumber, customerName, count(customerNumber) AS order_count
FROM (
	SELECT
		*
	FROM
		customers AS t1
	INNER JOIN orders AS t2 USING (customerNumber)
) AS t3
GROUP BY customerNumber
ORDER BY order_count DESC
LIMIT 1;

-- 문제 5-2
SELECT ccutomerNumber, cutomerName, count(*) order_count
FROM coustomers
NATURAL JOIN orders
GROUP BY customerNumber
HAVING order_count = (
	SELECT count(*) cnt
    FROM orders
    GROUP BY cutomerNumber
    ORDER BY cnt DESC
    LIMIT 1
);
-- 문제 6
SELECT * FROM products; -- productCode
SELECT * FROM orderdetails; -- productCode, orderNumber
SELECT * FROM orders; -- orderNumber, orderDate

SELECT DISTINCT
	productCode, productName
FROM (
	SELECT *
    FROM orderdetails AS t1
    INNER JOIN products AS t2 USING (productCode)
    INNER JOIN orders AS t3 USING (orderNumber)
) AS t4
WHERE YEAR(orderDate) ='2004'
ORDER BY productCode DESC; 

