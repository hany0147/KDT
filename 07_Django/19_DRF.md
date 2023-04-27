# Django - Django rest framewordk
## 1. 개요
### HTTP Request Methods
- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
- HTTP verbs라고도 함
1. GET: 서버에 리소스의 표현을 요청
2. POST: 데이터를 지정된 리소스에 제출, 서버 상태를 변경
3. PUT: 요청한 주소의 리소스 수정(UPDATE)
4. DELETE: 지정된 리소스를 삭제

### HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료되었는 지 여부를 나타냄
1. 100번 대: Informational responses
2. 200번 대: Successful responses
3. 300번 대: Redirection responses
4. 400번 대: Client error responses
5. 500번 대: Server error responses

## 2. REST API
- REST라는 API 디자인 아키텍처를 지켜 구현한 API

### API
- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법

### Web API
- 웹 서버 또는 웹 브라우저를 위한 API
- 하나부터 열까지 직접 개발하기 보다 여러 Open API를 활용하는 추세

### REST
- Representational State Transfer
- '소프트웨어 아키텍쳐 디자인 제약 모음'
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- REST 원리를 따르는 시스템을 `RESTful`하다고 부름
- **"자원을 정의"**하고 **"자원에 대한 주소를 지정"**하는 전반적인 방법 서술
1. 자원의 식별: url
2. 자원의 행위: HTTP Methods
3. 자원의 표현: 궁극적으로 표현되는 결과물(JSON으로 표현된 데이터 제공)

## 3. Response JSON

## N:1 Relation