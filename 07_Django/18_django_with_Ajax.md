# Django - django with Ajax
## 1. 개요
> 문서를 매번 받는 게 아니라, 문서를 **다시 그린다**

### 비동기
- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

### Ajax
- 비동기적인 웹 애플리케이션 개발을 위한 프로그래밍 기술명
  - 사용자의 요청에 대한 즉각적인 반응을 제공하면서, 페이지 전체를 다시 로드하지 않고 필요한 부분만 업데이트 하는 것을 목표

### XMLHttpRequest
- js 객체로, 클라이언트와 서버 간에 데이터를 비동기적으로 주고받을 수 있도록 해주는 객체
  - js 코드에서 서버에 요청을 보내고, 서버로부터 응답을 받을 수 있음

## 2. 비동기 요청
### Axios
- js에서 HTTP 요청을 보내는 라이브러리. 주로 프론트엔드 프레임워크에서 사용.