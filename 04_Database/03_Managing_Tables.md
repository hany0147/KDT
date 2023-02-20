# Managing Tables

## 1. Create a table

### CREATE TABLE문
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건 작성
  ```SQL
  CREATE TABLE table_name(
    column_1 data_type,
    column_2 data_type,
    ...,
    constraints
  );
  ```
#### 데이터 타입
1. Numeric: INT, FLOAT, ...
2. String: **VARCHAR**(가변), TEXT, CHAR(고정) ...
3. Date and Time: DATE, DATETIME, ...

#### 제약 조건
- 데이터 **무결성**을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙
  - 무결성: 데이터의 정확성과 일관성을 보증함
1. NOT NULL: NULL 허용 금지
2. PRIMARY KEY(): PK 설정

#### 속성
1. AUTO_INCREMENT: 테이블의 기본 키에 대한 번호 자동 생성
    - 시작 값 1, 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
    - 고유한 숫자 부여(기본 키 필드에 사용)
    - 이미 사용한 값은 재사용하지 않음
    - 기본적으로 NOT NULL 제약 조건 포함

## 2. Delete a table

### DROP TABLE문
- 테이블 삭제
  ```SQL
  DROP TABLE table_name;
  ```

## 3. Modifying table fields

### ALTER TABLE문
- 테이블 **필드 조작**(생성, 수정, 삭제)
1. ALTER TABLE **ADD**: 필드 추가(C)
    - 새 필드 이름과 데이터 타입 및 제약 조건 작성
    ```SQL
    ALTER TABLE
      table_name
    ADD
      new_column_name column_definition;
    ```
2. ALTER TABLE **MODIFY**: 필드 속성 변경(U)
    ```SQL
    ALTER TABLE
      table_name
    MODIFY
      column_name column_definition;
    ```
3. ALTER TABLE **CHANGE COLUMN**: 필드 이름 변경(U)
    - MODIFY의 기능까지도 내포함
    ```SQL
    ALTER TABLE
      table_name
    CHANGE COLUMN
      original_name new_name column_definition;
    ```
4. ALTER TABLE **DROP COLUMN**: 필드 삭제(D)
    ```SQL
    ALTER TABLE
      table_name
    DROP COLUMN
      column_name;
    ```
