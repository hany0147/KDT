-- 문제1
SELECT * FROM employees;
SELECT * FROM offices;

SELECT
	employeeNumber, lastName, firstName, city
FROM
	employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;
-- 문제 2
SELECT * FROM customers;
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
-- 문제 3
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
-- 문제 4
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers AS t1
INNER JOIN offices AS t2
	ON t1.city = t2.city
ORDER BY
	customerNumber DESC;
-- 문제 5
-- 1. INNER JOIN은 두 테이블에 동일한 officeCode가 있는 값만 추출한다.
-- 2. 반면, LEFT JOIN은 메인 테이블인 customers의 모든 값을 반환하고, 비교 테이블인 offices의 경우 customer의 officeCode가 일치하는 값만 반환한다.
	-- 따라서, offices에 존재하지 않는 레코드의 경우는 NULL값으로 반환한다.
-- 3. 따라서, RIGHT JOIN은 LEFT와 반대로 메인 테이블 대신 비교 테이블 offices의 값을 모두 반환하고 customers는 offices와 공통되는 부분만 반환한다.

-- 문제 6
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers AS t1
RIGHT JOIN offices AS t2
	ON t1.city = t2.city
UNION
SELECT
	customerNumber,
    officeCode,
    t1.city,
    t2.city
FROM
	customers AS t1
LEFT JOIN offices AS t2
	ON t1.city = t2.city    
ORDER BY customerNumber DESC;

-- 문제 7
SELECT * FROM orderdetails;
SELECT * FROM orders;
SELECT
	orderdetails.orderNumber, orderDate
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderdetails.orderNumber;
-- 문제 8
SELECT * FROM products;
SELECT
	orderNumber,
    t1.productCode,
    t2.productName
FROM
	orderdetails AS t1
INNER JOIN products AS t2
	ON t1.productCode = t2.productCode
ORDER BY
	orderNumber;
-- 문제 9
SELECT 
	t1.orderNumber, t3.productCode, t2.orderDate, t3.productName
FROM
	orderdetails AS t1
INNER JOIN orders AS t2
	ON t1.orderNumber = t2.orderNumber
INNER JOIN products AS t3
    ON t1.productCode = t3.productCode
ORDER BY
	orderNumber;