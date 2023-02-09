# # SQL 기초

## 1. SQL 
- Structure Query Language
- DB에 정보를 `저장`하고 `처리`하기 위한 프로그래밍 언어
- 테이블의 형태로 `구조화`된 RDB에게 `요청(질의)`하는 언어
- 결국 DB에서 Data를 `반환`하기 위한 언어

### SQL 문법
- SQL 키워드는 대소문자 구분하지 않음
  - 하지만 `대문자`로 작성하라
- SQL문 끝에는 `세미콜론`(;) -> 구분자

## 2. SQL Statements
```SQL
-- 기본 SQL문
SELECT column_name FROM table_name;
```
- 키워드(절): SELECT, FROM 등

### 유형
1. DDL(데이터 정의)
    - 구조를 정의하는 것
    - CREATE, DROP, ALTER
2. **DQL(데이터 검색)**
    - SELECT
3. DML(데이터 조작)
    - INSERT, UPDATE, DELETE
4. DCL(데이터 제어)
    - 권한이나 계정을 컨트롤하는 것
    - COMMIT, ROLLBACK, GRANT, REVOKE