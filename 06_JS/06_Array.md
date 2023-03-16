# JS - Array

## 1. 개요
- object는 순서형을 쓸 수 없다.
  - 따라서 배열이 필요하다.

### Array
- 순서가 있는 데이터 집합을 저장하는 자료구조(object + 순서)
- 배열의 키는 인덱스

### 구조
- 대괄호를 이용해 작성
- length(속성값)를 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음
- 배열 요소의 자료형엔 제약이 없음
- 배열의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음

```js
const fruits = ['apple', 'banana', 'coconut']

console.log(fruits[0])
console.log(fruits[1])
console.log(fruits[2])

console.log(fruits.length)
```
### 배열과 반복
```js
// for
// 인덱스 접근
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i])
}

//for...of
// 요소 접근
for (const fruit of fruits) {
  console.log(fruit)
}
```

## 2. 배열과 메서드
### push / pop
- 배열 끝 요소를 추가 또는 제거
- pop: 배열 끝 요소를 제거하고, 제거한 요소를 반환
- push: 배열 끝에 요소를 추가

### unshift / shift
- 배열 앞 요소를 추가 또는 제거
- shift: 배열 앞 요소를 제거하고, 제거한 요소를 반환
- unshift: 배열 앞에 요소 추가

### forEach
- **인자로 주어진** 함수(콜백 함수)를 배열 요소 각각에 대해 실행
- 배열의 메서드
- **콜백 함수**: 인자로 주어진 함수 / 다른 함수에 인자로 전달되는 함수
  - 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
  - 3가지 매개변수로 구성됨
    1. item: 배열의 요소
    2. index: 배열 요소의 인덱스
    3. array: 배열
- 반환 값: undefined

```js
array.forEach(function (item, index, array) {
  // do something
})
```

### map
- forEach + 반환값
- 배열 요소 전체를 대상으로 콜백함수를 호출하고, 함수 호출 결과를 모아 **새로운 배열을 반환**
```js
const result = array.map(function (item, index, array) {
  // do something
})
```

### 배열 정리
- 배열의 본질은 객체다!
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 동일
- 다만 배열의 키는 숫자라는 점!
- 숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드를 제공

### 배열 순회 종합
- for loop: 배열의 인덱스를 이용하여 각 요소에 접근
- for...of: 배열 요소에 바로 접근 가능
- forEach(사용권장): 간결하고 가독성 높음. callback함수를 이용하여 각 요소를 조작하기 용이.

## 99. 참고
### 콜백함수 구조를 사용하는 이유
- 함수의 재사용성 측면
- 비동기적 처리 측면
  - 다른 코드의 실행을 방해하지 않음