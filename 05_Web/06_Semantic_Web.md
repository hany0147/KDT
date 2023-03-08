# Web - Semantic Web
## 1. 개요

### Semantic Web
- 웹 데이터를 의미론적으로 표현하고 연결하는 개념
- 이 요소가 시각적으로 어떻게 보여질까? -> 이 요소가 가진 목적과 역할은 무엇일까?
- 인터넷을 위함(검색엔진 최적화)
## 2. Semantics in HTML
### h1
- 이 페이지의 최상위 제목
  - 페이지 최상위 제목 의미를 제공하는 semantic 요소
- **브라우저**의 의해 제목처럼 보이도록 큰 글꼴로 스타일이 지정됨
```HTML
<span style="font-size: 32px;">Heading</span>
<!-- 모든 요소를 최상위 제목처럼 보이게 할 수는 있으나 의미론적 가치는 없음 -->
```

### HTML Semantic Element
- 기본적인 모양과 기능 이외에 의미를 가지는 html 요소
- **검색엔진** 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어 줌
- 종류
  1. header
  2. nav
  3. main
  4. article
  5. section
  6. aside
  7. footer
- div: non-semantic
- strong: 강조의 의미가 담김
  - 반면 `b`는 의미가 없고 볼드체라는 기능(스타일)만 있음

## 3. Semantics in CSS
### OOCSS
- Object-Oriented CSS
- 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

### BEM
- Block Element Modifier
- 블록, 요소, 수정자를 사용해 클래스 이름을 구조화하는 방법론
- block
  - 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너
  - 재사용을 위해 margin 또는 padding을 적용하지 않음
- element
  - block이 포함하고 있는 한 조각
  - 블록을 구성하는 종속적인 하위요소
- modifier
  -block 또는 element의 속성

```CSS
.block {}
.block__element {}
.block--modifier {}
```

## 99. 참고
### 의미론적 마크업의 이점
- 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
- 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 추가적으로 도움

### 클래스 이름이 너무 길어지는 건 아닐까?
- 괜찮음. 분명하게 전달할 수 있는가가 중요함.
- 빠르고 명확하게 표기하는 게 우선적임
- 너무 고민하지 않는 것도 중요

### 목적
- 재사용 가능한 모듈로 분리함으로써 유지 보수성과 학장성을 향상
- 개발자 간의 협력이 향상되어 공통 언어와 코드 이해를 확립

## 두 방법론 섞은 예시
- [에어비엔비_CSS] <https://github.com/airbnb/css#oocss-and-bem>
  - [한국어번역] <https://github.com/CodeMakeBros/css-style-guide>

## 흑마술
- emmet_cheat_sheet <https://docs.emmet.io/cheat-sheet/>
- 한 줄 지우고 싶을 떄: 해당 줄 아무 곳에나 커서를 놓고 컨트롤 + L 누르면 됨 