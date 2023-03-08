# Web - Fundamentals of Bootstrap

## 1. 개요
### Bootstrap
- 프론트엔드 라이브러리(Toolkit)
- 반응형 웹 디자인 & CSS 및 JS 기반의 `컴포넌트`와 스타일 제공
  - 컴포넌트: 여러 개의  프로그램 함수들을 모아 하나의 특정한 기능을 수행할 수 있도록 구성한 작은 기능적 단위
    - 함수/모듈과 유사
```html
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  </head>
  <body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
```
> 공식문서를 통해 일련의 규칙을 학습해야 한다.
- 예시
  ```html
  <h2 class="mt-5">hi</h2>
  ```

## 2. Typography
- 클래스로 표현한다.
- 클래스의 스타일은 이미 정해져 있다.
  - 따라서 공식 문서를 확인하라.

### Bootstrap Color system 
- 부트스트랩이 지정하고 제공하는 색상 시스템

## 3. Component
- 부트스트랩에서 제공하는 **UI 관련 요소**
- 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험을 위하여

## 99. 참고
### CDN
- Content Delivery Network
- `지리적 제약 없이` 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
  - 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)

### 사용 하는 이유
- 손쉬운 반응형 웹 디자인 구현
- 빠른 개발과 유지보수
- 크로스 브라우징 지원