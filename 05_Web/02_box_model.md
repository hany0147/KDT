# Web - The box model
## 1. 개요
## CSS Box Model
- 모든 HTML 요소를 **(사각형)** 박스로 표현

## 2. 구성 요소
- 박스에 대한 크기, 여백, 테두리 등의 스타일을 지정하는 디자인 개념
### BOX의 구성
- Margin: 가장 바깥쪽 영역
  - 박스의 테두리가 아님
  - 박스의 외부 영역(이 박스와 다른 요소 사이의 공백)
  - 마진의 값을 키우면, 다른 요소와 박스가 멀어짐
- Border: 콘텐츠와 패딩을 감싸는 테두리 영역
- Padding: 콘텐츠 주위에 위치하는 공백 영역
  - 값이 커지면, 테두리와 내용이 서로 멀어짐
- Content: 콘텐츠가 표시되는 영역

### Box 구성의 방향 별 명칭
- content 외, top, bottom, right, left
- content는 height, width

- div: 구역 나누기 위한 태그
- 비운다는 개념보다는 채운다의 개념을 장착하자.

### width & height 속성
- 박스의 크기를 조정하는 게 아니라 콘텐츠의 크기를 조정하는 것

### box-sizing 속성
- 요소의 너비와 높이를 계산하는 방법을 지정
```CSS
* {
  box-sizing: border-box;
}
```

## 3. 박스 타입
```CSS
.index {
  display: block;
  display: inline;
}
```
0. Normarl flow: CSS를 적용하지 않았을 경우 Block 및 Inline요소가 기본적으로 배치되는 방향
  - block은 위에서 아래
  - inline은 왼쪽에서 오른쪽
1. Block
  - block은 한 줄 영역을 다차지 하기 때문에 다음 박스는 아래로 내려가게됨. 들어 갈 곳이 없어서.
    - 기본적으로 width 속성을 지정하지 않으면 박스는 인라인 방향으로 사용가능한 공간 모두 차지.
  - block요소는 기본적으로 부모 요소 너비의 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다.
  - block 요소의 총 너비와 총 높이는 content + padding + border(상하 혹은 좌우 두께)
  - h1, p, div 등
2. Inline
  - span: 인라인계의 div
  - 자기 콘텐츠의 너비와 높이만 차지한다.
  - width나 height 속성을 지정할 수 없다.    
  - a, span, img
    - 단, 이미지는 다른 inline 요소들과 달리 width나 height 값을 지정할 수 있다.
  - 만약 inline 요소의 크기를 제어하려면 block으로 변경해버리거나, `inline-block` 요소로 설정해주어야 한다.
  - 수직 방향
    - padding, margins, borders가 적용되지만 **다른 요소를** 밀어낼 수 없음
  - 수평 방향
    - 동일하게 적용되며, 다른 요소를 밀어낼 수 **있음**


## 99. 참고
### Shorthand 속성
1. border
```CSS
border: 1px solid black;
```

2. margin & padding
- 4개: 상우하좌 (시계방향)
- 3개: 상 /좌우/ 하
- 2개: 상하/좌우
- 1개: 공통

### display: inline-block
- 요소가 줄 바꿈 되는 것을 원하지 않으면서(inline), 너비와 높이를 적용하고 싶은 경우(block)에 사용
- blcok 요소의 특징을 가짐
  - 니버 및 높이 속성이 준수
  - 패딩, 여백, 테두리로 인해 다른 요소가 밀려남

### Margin collapsing(마진 상쇄)
- 마진 상하가 만나 큰 margin으로 결합되는 현상
  - 두 요소다 block 타입이어야 하며,
  - 상하로 만나야 함