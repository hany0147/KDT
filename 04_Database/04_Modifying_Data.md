# Modifying Data

## 1. Insert data into table

### 👍INSERT문
- 테이블 이름 뒤 괄호 안에 필드 목록 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성
    ```SQL
    INSERT INTO table_name (c1, c2, ...)
    VALUES (V1, V2, ...);
    ```
- CURDATE()

## 2. Update data in table

### 👍UPDATE문
- 테이블 레코드 수정
- SET절 다음에 수정할 필드와 새 값을 지정
- WHERE절에서 수정 할 레코드를 지정하는 조건 작성(쓰지 않으면 모든 레코드 수정하게 됨)
    ```SQL
    UPDATE table_name
    SET column_name = expression,
    [WHERE
      condition];
    ```
## 3. Delete data from table

### 👍DELETE문
```SQL
DELETE FROM table_name
[WHERE
  condition];
```