# Nested Queries
## 1. Introduction to Subquery
> Nested: 중첩된

<BR>

### Subquery
- A query inside a query
- 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
```SQL
DELETE FROM table1
WHERE age = (
  SELECT MIN(age) FROM table1
);
```
- 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
- 다양한 절 등에서 다양한 맥락에서 사용 가능
> FROM절의 서브쿼리는 `파생된` 테이블로 인식하므로 **별칭(AS)**을 적용해야 함. 

<BR>

### EXISTS 연산자
- 쿼리문에서 반환된 레코드의 존재 여부 확인
```SQL
SELECT 
  select_list
FROM
  table
WHERE
  [NOT] EXISTS (subquery);
```
- 어디서나 쓰일 수 있지만, 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는 데 사용

## 2. Conditional Statements

<br>

### CASE문
- SQL문에서 조건문을 구성
```SQL
CASE case_value
  WHEN when_value1 THEN statements
  WHEN when_value1 THEN statements
  ...
  [ELSE else-statements]
END CASE;
```
- ELSE 절을 쓰지 않아도 되지만,
  - ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생


## 99. 참고
- REGEXP (정규표현식) -> 공부 바람
```SQL
WHERE city REGEXP '^[aeiou]';
```
- 정규표현 생성기의 도움을 받을 수도 있다.
- 정규표현식 사이트 <https://regexr.com/>