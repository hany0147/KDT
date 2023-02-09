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