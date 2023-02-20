# Multi Table Queries

## 1. Introduction to Join
- **외래 키**: 연결을 위한 장치
- 관리 용이
- 하지만 테이블을 한 개 밖에 출력할 수 없어 다른 테이블과 연결지어 출력하는 것이 필요함.
  - **JOIN**
  - N : 1 관계 -> 개념 공부 필요
    - FK는 N 쪽에 있다(N쪽에서 1을 **참조**한다)

## 2. Joining tables
### JOIN문
- 둘 이상의 테이블에서 데이터를 검색하는 방법

#### 💡 INNER JOIN절
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
  - **교집합**
- FROM절 이후 메인 테이블 지정
- INNER JOIN절 이후 메인 테이블과 조인할 테이블 지정
- ON 키워드 이후 조인 조건을 작성
```SQL
SELECT
  select_list
FROM
  table1
INNER JOIN table2
  ON table1.fk = table2.pk;
```

#### 💡 LEFT JOIN절
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
- 일치하지 않으면 NULL 값으로 나옴
- 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 왼쪽 레코드를 여러 번 표시.
```SQL
SELECT
  select_list
FROM
  table1
LEFT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
```

#### 💡 RIGHT JOIN절
- 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환
```SQL
SELECT
  select_list
FROM
  table1
RIGHT [OUTER] JOIN table2
  ON table1.fk = table2.pk;
```

#### UNION, UNION ALL (검색 바람)
- The query above depends on the UNION **set operator** to remove duplicate rows introduced by the query pattern.
- We can avoid introducing duplicate rows by using an anti-join pattern for the second query, and then use a UNION ALL set operator to combine the two sets. In the more general case, where a full outer join would return duplicate rows, we can do this: (UNION ALL)


#### USING (검색 바람)
```SQL
INNER JOIN orders USING (orderNumber)
```

#### NATURAL JOIN (검색 바람)
```SQL
NATURAL JOIN orders
```
