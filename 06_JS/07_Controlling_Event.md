# JS - Controlling Event

## 1. 개요

### 웹에서의 이벤트
- 버튼을 클릭했을 때 / 모달이 출력되는 것
- 마우스 커서의 위치에 따라 / 드래그 앤 드롭하는 것
- 사용자가 입력한 값에 따라 / 새로운 요소를 생성하는 것
> 일상생활에서의 이벤트처럼 웹에서도 이벤트를 통해 **특정 동작을 수행**한다.

## 2. 이벤트
### event
- 무언가 일어났다는 신호, 사건(모든 DOM 요소는 이러한 신호를 만들언 냄)
- DOM 요소는 event를 받고 받은 event를 `처리`할 수 있음
  - 이벤트 핸들러(처리기)

### event handler
- 이벤트가 발생했을 떄 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것
#### .addEventListener()
- 대표적인 이벤트 핸들러 중 하나
- 특정 이벤트를 DOM 요소가 수신할 떄마다 콜백 함수를 호출
- 처리기를 DOM 요소에 붙여야 함
```js
EventTarget.addEventListener(type, handler)

// EventTarget: DOM 요소, type: 특정 이벤트, handler: 콜백 함수
// 대상에 특정 event가 발생하면, 할 일을 등록한다.
```
- type: 이벤트 이름(이미 정해져 있음)
  - <https://developer.mozilla.org/en-US/docs/Web/Events>
- handler: 발생한 이벤트 객체를 수신하는 콜백 함수 / 콜백 함수는 발생한 event object를 유일한 매개변수로 받음

## 3. 이벤트 핸들러 활용
