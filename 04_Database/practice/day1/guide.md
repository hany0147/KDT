# MySQL Workbench 활용 가이드

## 1. Workbench 활용 MySQL 접속 방법(윈도우 기준) 
- CLI
1. 명령프롬프트 실행
2. 경로 확인 및 실행(C:\Program Files\MySQL\MySQL Workbench 8.0>MySQLWorkbench.exe)

-  GUI
1. `MySQL Workbench 8.0 CE` 아이콘 클릭

- 공통

1. 접속

![](image\01.jpg)

2. 데이터 불러오기
    1. Administration 창으로 바꾼 뒤, `MANAGEMENT` - `Data Import/Restore` 클릭
    2. 원하는 파일을 불러오기 위해, `Import from Self-Contained File`을 체크하고 해당 파일을 불러온다.
    3. 우측 하단 `Start Import`를 클릭하고 `import completed`를 확인

![참고](image\02.jpg)

3. 데이터 확인
    1. Schemas 창으로 바꾼 뒤, 불러온 DB 파일을 더블 클릭합니다.
    2. 하위 파일 중 테이블을 클릭하면 각 테이블들을 확인할 수 있다.
-------------

## 2. (실습 DB에 대한) 쿼리문 작성 및 쿼리문 실행 방법

1. `classicmodels` DB를 더블클릭하여 선택함.
2. `Query` 창을 켠다.
    - Query창은 마치 vscode의 코드 입력창과 유사하다.
3. 쿼리문 입력
    ```SQL
    SELECT * FROM customers;
    ```
4. 쿼리 실행
    - 번개 모양을 누른다(터미널과 원리 동일)
    - 혹은 좌측 Schemas 창에서 clssicmdoels-Tables-원하는 테이블에 커서를 올린 후, 우측에 `번개 + 테이블`을 누르면 해당 쿼리문과 함께 테이블이 조회됨. 

## 3. 참조
- 테이블의 우측 `설정` 그림을 클릭하면 해당 테이블의 PK 등을 설정할 수 있다.
