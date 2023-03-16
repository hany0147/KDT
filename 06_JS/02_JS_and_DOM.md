# JS - Javascript and DOM
## 1. JavaScript 개요
- 웹 브라우저에 내장된 JS 엔진에 의해 브라우저에서 실행됨

### JS 실행환경
1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console

## 2. DOM 기본 개념
- Document Object Model
- 웹 페이지를 구조화된 객체로 제공하며 **프로그래밍 언어가 웹 페이지를 사용할 수 있게** 연결시킴
- 일종의 API
- 웹 페이지의 구성 요소를 제공함
- 문서는 웹 브라우저를 통해 해석되어 화면에 나타남. DOM은 이러한 문서를 조작하는 방법을 제공하는 API
- 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체의 트리로 구조화 함
- 모두 document 객체의 자식

> 웹 페이지를 동적으로 만드는 것 == 웹 페이지를 `조작`하는 것
- 조작하기 위한 순서
    1. 조작하고 하는 요소를 **선택** 또는 **탐색**
    2. 선택된 요소의 콘텐츠 또는 속성을 **조작**(생성, 추가, 삭제)

### 'document' object
- 웹 페이지 객체
- DOM Tree의 진입점
- 페이지를 구성하는 모든 객체 요소 포함

## 3. DOM Query(선택)
1. 요소 하나 선택
    - document.querySelector()
      - 제공한 선택자와 일치하는 element 한 개 선택
      - 제공하는 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)
2. 요소 여러개 선택
    - document.querySelectorAll()
      - 여러 element 선택
      - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
      - NodeList를 반환

## 4. DOM Manipulation(조작)
### 조작 목차
1. 속성 조작
    - 클래스 속성 조작
    - 일반 속성 조작
2. HTML 콘텐츠 조작
3. DOM 조작
4. style 조작

### 속성 조작
#### 클래스 속성 조작
- 'classList' property: 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
- 메서드: .add(), .remove()