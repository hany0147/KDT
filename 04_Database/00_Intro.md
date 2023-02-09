# Database 소개

## CRUD

# The Relation(관계)

## Relational Database
- 데이터 간에 관계가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- 관계: `논리적 연결`

- 데이터의 고유한 식별 값: `기본 키(Primary Key; PK)`
- PK값을 참조(참고)하는 키: `외래 키(Foreign Key; FK)`

### 용어
1. Table(Relation): 데이터를 기록하는 곳
2. Field(Column, Attribute): 각 필드에 고유한 데이터 형식(타입)이 지정됨
3. Record(Row, Tuple): 구체적인 데이터 값이 저장됨.
4. Database(Schema): 테이블의 집합
    - Table != DB
5. Primary Key: 각 레코드의 고유한 값, 레코드의 `식별자`로 활용, `중복 없음`
6. Foreign Key: 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키, `관계를 만드는` 데 사용

## RDBMS
- Relational Database Management System
- DB와 사용자 간의 인터페이스 역할
- 종류: `MySQL`, PostgreSQL, Oracle DB, MS SQL Server 등

### MySQL
- 가장 널리 사용되는 오픈 소스 RDBMS

