# Single Table Queries
## 1. Querying data

- 테이블에서 데이터를 조회
  - SELECT 다음에 데이터를 선택하려는 필드(열)를 하나 이상 지정
  - FROM 다음에 데이터를 선택혀라는 테이블의 이름을 지정
```SQL
SELECT
  select_list
FROM
  table_name;
```
- NULL: 데이터 없음
- `AS` 키워드: 별칭
- `--`(더블 하이픈)이 주석임
- 기본적인 사칙연산 사용 가능 

## 2. Sorting data
- `ORDER BY` clause: 조회 결과의 레코드를 정렬
  - `[]`: 선택사항을 의미함 
  - `|`: or 을 의미함
  - ASC(오름차순, 기본값), DECS(내림차순)

## 3. Filtering data
- 중복 제거, 조건 설정

### Clause
1. DISTINCT: 조회 결과에서 중복된 레코드를 제거
    - SELECT 바로 뒤에 위치함
    ```SQL
    SELECT DISTINCT
      select_list
    FROM
      table_name;
    ```

2. WHERE: 조회 시 특정 검색 **조건**을 지정
    - FROM절 뒤에 위치
    - 조건(search_condition)은 비교연산자 및 논리연산자가 들어감
    ```SQL
    SELECT
      select_list
    FROM
      table_name
    WHERE
      search_condition;
    ```
    
    - IS -> NULL값과 같이 쓰이는 편
    - 정규 표현식

3. LIMIT: 조회하는 레코드 수를 제한
    - 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
    - row_count는 조회할 최대 레코드 수를 지정
    ```SQL
    SELECT
      select_list
    FROM
      table_name
    LIMIT [offset,] row_count;
    ```
## 4. Grouping data
1. GROUP: 레코드를 **그룹화**하여 **요약**본 생성 with **집계 함수**(Aggregation Funtions)
    - 집계 함수: 값에 대한 계산을 수행하고 **단일한** 값을 반환하는 함수
      - SUM, AVG, MAX, MIN, COUNT
    - FROM 및 WHERE절 뒤에 배치
    - GROUP BY절 뒤에 그룹화할 필드 목록을 작성

    ```SQL
    SELECT
      c1, c2,..., cn, aggregate_function(ci)
    FROM
      table_name
    GROUP BY
      c1, c2, ..., cn;
    ```
2. HAVING: 집계 항목에 대한 세부 조건을 지정

## 99. 참고
- 정렬에서의 NULL: 존재할 경우, 오름차순 정렬 시 결과에 NULL이 먼저 출력