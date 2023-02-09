# RDBMS 용어 정리

1. Table(Relation): 데이터를 기록하는 곳
2. Field(Column, Attribute): 각 필드에 고유한 데이터 형식(타입)이 지정됨
    - 필드 중 하나로 PK를 지정하고, FK를 지정하여 각 테이블을 연결함.
3. Record(Row, Tuple): 구체적인 데이터 값이 저장됨.
4. Database(Schema): 테이블의 집합
    - Table != DB
5. Primary Key: 각 레코드의 고유한 값, 레코드의 `식별자`로 활용
    - `중복 없음`
    - `Null값`이 있어서는 안 됨.
6. Foreign Key: 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
    - `관계를 만드는` 데 사용
    - PK와 달리 한 테이블에서 여러 개의 FK를 가질 수 있음.