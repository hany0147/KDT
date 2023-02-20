# SQL 심화
## 1. Transactions
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
- 다 성공하던가 다 실패하던가 해야함(All or Nothing)
- 임시 데이터 영역을 가지고 있음.
- 쪼개질 수 없는 업무처리의 단위

```SQL
START TRANSACTION;
sate_ments;
...
[ROLLBACK|COMMIT];
```
- COMMIT: 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
- ROLLBACK: 부분적으로 작업이 실패하면 트랜잭션에 진행한 모든 연상을 취소하고 트랜잭션 실행 전으로 되돌림

## 2. Triggers
- 특정 이벤트(INSERT, UPDATE, DELETE)에 대한 응답으로 자동으로 실행되는 것
- 트리거는 DML의 영향을 받는 필드 값에만 적용할 수 있음
- 무언가 변화할 때 ~하겠다.
  - ~를 추가한 후에 ~하겠다
  - ~를 수정하기 전에 ~하겠다

```SQL
CREATE TRIGGER trigger_name
  {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
  ON table_name FOR EACH ROW
  trigger_body;
```
- `COMMIT`되기 전 OR 된 후로 접근해야 함.
- 트리거는 특정 시점 전/후의 값에 접근 할 수 있도록 제공하는 키워드: OLD | NEW
- 트리거가 활성화 될 때 실행할 코드를 trigger_body에 지정
  - 여러 명령문을 실행하려면 `BEGIN-END` 키워드로 묶어서 사용
  - `DELIMITER` : 종료 구문을 바꿔줌.
    - **DELIMITER //** -> 여기서부터 //을 종료 구문으로 하겠다.

### 트리거 목록 확인
```SQL
SHOW TRIGGERS
```

### 트리거 삭제
```SQL
DROP TRIGGER triger_name;
```

### 트리거 생성 시 에러 해결
- 트랜잭션 생성 후 정상적으로 종료되지 않아 발생하는 에러 발생 시 해결법

```SQL
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```