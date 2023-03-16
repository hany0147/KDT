# JS - Functions
## 1. 개요
### Function
- `참조 자료형`에 속하며 모든 함수는 Function object

### 구조
```JS
function name ([param[, param[, param[,..., param]]]]) {
  statements
  return value
}
```
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement
- return이 없다면 undefined를 반환

## 2. 함수의 정의
### 1. 선언식(declaration)
```js
function funcName () {
  statements
}
```

### 2. 표현식(expression)
```js
const funcName = function () {
  statements
}
// function () {statements} -> 익명 함수
```
- 선언식과 달리 표현식으로 정의한 함수는 **호이스팅 되지 않으므로** 코드에서 나타나기 전에 먼저 사용할 수 없음
  - 따라서 표현식 사용 권장

### 기본 함수 매개변수(Default function parameter)
- 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
```js
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting() // Hi Anonymous
```

### 매개변수와 인자의 개수 불일치
```js
// 매개변수 개수 < 인자 개수
const noArgs = function () {
  return 0
}
console.log(noArgs(1, 2, 3)) // 0

const twoArgs = function (num1, num2) {
  return [num1, num2]
}
console.log(twoArgs(1, 2, 3)) // [1, 2]
```
```js
// 매개변수 개수 > 인자 개수
const threeArgs = function (num1, num2, num3) {
  return [num1, num2, num3]
}
console.log(threeArgs(1)) // [1, undefined, undefined]
```

### 나머지 매개변수(Rest parameters)
- 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법
- `...`으로 나타냄
- 함수 정의에는 하나의 나머지 매개변수만 있을 수 있음
- 나머지매개변수는 함수 정의에서 마지막 매개변수여야함
```js
const myFunc = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs]
}

console.log(myFunc(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
console.log(myFunc(1, 2)) // [1, 2, []]
```

### 화살표 함수 표현식(Arrow function expressions)
- 함수 표현식의 간결한 표현법

#### 작성 순서
1. function키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
2. 함수의 **매개변수가 하나 뿐이라면** 매개변수의 `()`의 제거 가능
    - 권장하지 않음
3. 함수 본문의 **표현식이 한 줄이라면** `{}`와 `return` 제거 가능
```js
const arrow1 = (name) => {
  return `hello, ${name}`
}
console.log(arrow1('harry'))

const arrow2 = (name) => `hello, ${name}`
console.log(arrow2('harry'))
```    
> 제약 때문에 주로 1단계만 씀

## 99. 참고
### 화살표 함수 표현식 응용
- 인자가 없다면 () or _ 로 표시 가능
- object를 return 한다면 return 을 명시적으로 작성해야 함
  - return을 적지 않으려면 소괄호로 감싸야 함