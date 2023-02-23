# Fundamentals of HTML and CSS
## 1. Introduction of Web page
- World Wide Web
- Web site: Web page가 모인 것, 사용자들에게 정보나 서비스를 제공하는 공간
- Web page: HTML, CSS, JS 등의 웹 기술을 이용하여 만들어진 하나의 인터넷 문서
  - HTML: Structure
  - CSS: Styling
  - JavaScript: Behaviour

## 2. Structuring the Web
### 2-1 Introduction to HTML
### HTML
- HyperText Markup Language
- 웹페이지의 의미와 구조를 정의하는 언어

#### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

#### Markup Language
- 태그 등을 이용하여 문서나 데이터의 **구조를 명시**하는 언어
  - HTML, MarkDown

### 2-2 Structure of HTML
#### HTML Element
```HTML
<p>My cat is very grumpy</p>
```
- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시(/)가 포함됨
  - 닫는 태그가 없는 태그도 존재: 안에 내용을 넣는 태그가 아닐 경우

#### HTML Attributes
```HTML
<p class = 'editor-note'>My cat is very grumpy</p>
```
- 태그에 추가적인 기능이나 정보를 기입하는 것
- 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
- 속성 값은 열고 닫는 따옴표로 감싸야 함
##### 목적
- 나타내고 싶지 않지만 추가적인 기능, 내용 담고 싶을 때 사용
- CSS가 해당 요소를 선택하기 위한 값으로 활용됨

#### HTML 문서의 구조
```HTML
<!doctype heml>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My page</title>
</head>
<body>
  <p>This is my page</p>
</body>
</html>
```
- `<!DOCTYPE html>`: 해당 문서가 HTML 문서라는 것을 나타냄
- `<html></html>`: 전체 페이지의 콘텐츠를 포함, 최상위 태그
- `<head></head>`: HTML 문서에 관련된 설명, 설정 등 / 사용자에게 보이지 않음 / 이 문서의 Settings
- `<body></body>`: 페이지에 표시되는 모든 콘텐츠
- `<title></title>`: 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- `<p></p>`: paragraph(문단)의 약자
- `<a href=""></a>`: anchor (하이퍼 링크)
- `<img scr="" alt="">` 이미지 / alt는 링크가 잘못되었거나 사진이 사라졌을 때 대신 쓸 내용(시각장애인들이 주로 이용함)

> ! 또는 html: 5를 입력하면 자동으로 양식이 만들어짐

### 2-3 Text Structure
- HTML의 주요 목적 중 하나는 텍스트 **구조와 의미를 제공**하는 것
```HTML
<h1>Main Heading</h1>
<!-- 문서의 최상위 제목 -->
```
- h1~h6, p
- List: ol(오더리스트의 약자), ul(언오더리스트), li
- Emphasis & Importance: emp, strong

## 3. Styling the web
### 3-1 Introduction to CSS
#### CSS
- Cascading Style Sheet
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어
```CSS
h1 { /* 선택자 */
  color: blue; /* 속성: 값*/
  font-size: 15px;
}
```
- 적용 방법
  1. 인라인 스타일: 태그의 속성으로 들어감
  ```HTML
  <h1 style="color: blue; background-color: yellow;">Hello World!</h1>
  ```
  2. 내부 스타일 시트: 헤드 부분에서 쓰기(style 태그)
  ```HTML
  <head>
    ...
    <style>
      h1 {
        color: blue;
      }
    </style>
  </head>
  ```
  3. 외부 스타일 시트: 별도의 CSS 파일 생성 후 불러오기(link 태그)
  ```HTML
  <link rel="stylesheet" href="style.css">
  ```
### 3-2 Select elements
#### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 함
- 종류
  - 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자: 지정한 모든 태그 선택
    - **클래스(class)** 선택자: 주어진 클래스 속성을 가진 모든 요소를 선택. 여러 곳에 쓰일 때 쓰임(.)
    - 아이디(id) 선택자: 의미상 한 곳에서만 쓰이고 있다고 정함(#)
      - 실제로는 여러 곳에서 동작가능하지만 코드 보수상 한 곳에서만 쓰인다는 의미를 부여함.
    - 속성(attr) 선택자
  - 결합자
    - 자손 결합자(" " (space)): 첫 번째 요소의 자손 요소들 선택
    - 자식 결합자(>): 첫번째 요소의 직계 자식만 선택

### 3-3 Cascade & Specificity
- 계단식 & 우선순위
#### Cascade
- 동일한 우선순위를 같는 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용

#### Specificity
- 선택자 별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용
- 우선순위가 높은 순
  1. Imortance(!imortant)
  2. 우선 순위: **인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자**
  3. 소스 코드 순서

#### 상속
- 부모 요소의 속성을 자식에게 상속함
- 이를 이용해 코드의 재사용성을 높임
- 상속 되는 속성
  - Text 관련 요소(font, color, text-align)
  - opacity
  - visibility 등
- 상속되지 않는 속성
  - 배치와 관련된 요소

## 99. 참고
### HTML 관련 사항
- 요소 이름은 소문자 사용을 권장
- 큰 타옴표 권장
- 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 주의

### CSS 관련 사항
- CSS 인라인 스타일은 사용하지 말 것
  - 문서 유지보수가 힘들어짐
  - CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드 이해를 어렵게 만듦
- CSS의 모든 속성 외우지 마
  - 주로 활용하는 속성 위주로 학습
  - Global CSS property Usage
- 속성은 되도록 class만 사용하도록 함
  - 개발 시 id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워짐
  - 문서에서 단 한번 유일하게 적용될 스타일의 경우에만 id 선택자 사용 **고려**
- CSS 상속 여부는 MDN 문서에서 확인
  - MDN 각 문서 하단에 속성별로 상속 여부를 확인할 수 있음
  - 웹공부: 뒤에 꼭 'mdn'을 꼭 붙여서 검색하라 / 표준임
    -[MDN](https://developer.mozilla.org/ko/)