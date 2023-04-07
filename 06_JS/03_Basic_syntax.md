# JS - Basic syntax of JavaScript
## 1. 변수
- 식별자 작성 규칙
  - 반드시 문,자 $ 또는 _로 시작
  - 대소문자 구분, 클래스 명 외에는 모두 소문자로 시작
  - 예약어 사용 불가
  - 카멜 케이스: 변수, 객체, 함수에 사용
  - 파스칼 케이스
  - 대문자 스네이크 케이스

### 변수 선언 키워드
1. let
    - 블록 스코프를 갖는 지역 변수를 선언
    - 재할당 가능 & 재선언 불가능
2. const
    - 블록 스코프를 갖는 지역 변수를 선언
    - 재할당 불가능 & 재선언 불가능
3. ~~var~~

#### 블록 스코프
- if, for, 함수 등의 중괄호 내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

> 기본적으로 const 사용 권장
> 재할당해야 하는 경우만 let 사용

## 2. 데이터 타입
### 1. 원시 자료형
  - Number, String, Boolean, undefined, null
  - 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
  1. Number: 정수 또는 실수형 숫자를 표현하는 자료형
  2. String: 덧셈을 통해 문자열끼리 붙일 수 있음, Template Literal(`${변수}`)를 사용하여 문자열 사이에 변수 삽입 가능
  3. null: 변수의 값이 없음을 **의도적**으로 표현할 때 사용 / object로 출력됨(버그)
  4. undefined: 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
  5. Boolean: true와 false / 자동 형변환 규칙에 따라 true 또는 false로 변환됨
### 2. 참조 자료형
  - Objects(Object, Array, Function)
  - 객체의 주소가 저장되는 자료형(가변, 주소가 복사)

## 3. 연산자
### 할당 연산자
- Increment(++): 피연산자의 값을 1 증가시키는 연산자
- Decrement(--): 피연산자의 값을 1 감소시키는 연산자
- 일치 연산자(===)만 써라

## 4. 조건문
```js
if (조건문) {
  명령문
} else if (조건문) {
  명령문
} else {
  명령문
}
```

## 5. 반복문
### while
- 조건문이 참이기만 하면 문장을 계속해서 수행
```js
while (조건문) {
  // do something
}
```
### for
- 특정 조건이 거짓으로 판별될 떄까지 반복
```js
for ([초기문]; [조건문]; [증감문]) {
  // do something
}
```
### for...in
- 객체(object, 참조 자료형 객체)의 속성을 순회할 때 사용
- 객체용 반복문
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
```js
for (variable in object) {
  statements
}
```
### for...of
- 반복 가능한 객체(배열, 문자열 등)를 순회할 떄 사용
```js
for (variable of object) {
  statements
}
```
> for...in은 `속성 이름`을 통해 반복 (배열을 반복하려 하면 인덱스를 반복해버림)
> for...of는 `속성 값`을 통해 반복

## 99. 참고
### 세미콜론
- js는 세미콜론 선택적 사용 가능
- 세미콜론이 없으면 ASI(자동 세미콜론 삽입 규칙)에 의해 자동으로 세미콜론이 삽입됨

### var
- 재할당 가능, 재선언 가능
- ES6 이전에 변순 선언시 사용하던 키워드
- **호이스팅**되는 특성으로 인해 예기치 못한 문제 발생 가능
- 함수 스코프를 가짐(블록 스코프가 아님)
- 변수 선언시 키워드 사용하지 않으면 자동으로 var로 선언됨

### 함수 스코프
- 함수끼리로 영역이 나눠짐
- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

### 호이스팅(hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
- var로 선언된 변수는 선언 이전에 참조할 수 있음
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

### 템플릿 리터럴(Template literals)
- 내장된 표현식을 허용하는 문자열 작성 방식
- ES6+부터 지원
- Backtic(``)을 이용하여, 여러 줄에 걸쳐 무자열을 정의할 수도 있고, 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김

### NaN을 반환하는 경우
1. 숫자로서 읽을 수 없음
2. 결과가 허수인 수학 계산식
3. 피연산자가 NaN
4. 정의할 수 없는 계산식
5. 문자열을 포함하면서 덧셈이 아닌 계산식

### 반복문 사용 시 const 및 let
- for 문
  - 재할당하니까 const를 사용하면 에러 발생
- for...in, for...of
  - 매 반복시 해당 변수를 새로 정의하여 사용하므로 const를 사용해도 에러가 발생하지 않음
  - let, const 상관없음