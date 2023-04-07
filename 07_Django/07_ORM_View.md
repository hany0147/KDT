# Django - ORM with view

## 1. READ
### 전체 게시글 조회

### 단일 게시글 조회

> TIME_ZONE = 'Asia/Seoul'
## 2. CREATE
- 사용자의 입력을 받는 페이지를 렌더링
- 사용자가 입력한 데이터를 받아 DB에 저장

## 3. HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지 나타내는 것

> 데이터 저장 후 유저를 어디론가 다시 보내야 한다.
### redirect()
- 인자에 작성된 주소로 다시 요청을 보냄

### HTTP
- 네트워크 상에서 데이터를 주고 받기위한 약속

### 'GET' method
- 특정 리소스를 조회하는 요청
- GET으로 데이터를 전달하면 Query String 형식으로 보내짐
- 반드시 데이터를 가져올 때만 사용해야 함(**조회할 때만** 사용)
- a 태그는 항상 GET 메서드만 사용
- SQL문의 SELECT 역할
- 브라우저마다 다르지만 길이제한이 있다
### 'POST' method 
- 특정 리소스에 변경사항을 만드는 요청
- POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐
- 조회 제외한 나머지에 쓰임
- 길이 제한이 없다
#### CSRF
- 사이트간 요청위조

## 4. DELETE
## 5. UPDATE
## 99. 참고
- 메서드: GET, POST, DELETE, PATCH, PUT