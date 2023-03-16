# JS - Object
## 1. 개요
### Object
- 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
> 타입으로써의 객체이다. 객체지향언어의 그 객체와 다르다.

### 객체의 구조
- 중괄호를 이용해 작성
- 중괄호 안에는 key:value쌍으로 구성된 속성을 여러 개 넣을 수 있음
- key는 **문자형**, value는 **모든 자료형**이 허용
- trailing comma(,): 속성을 추가, 삭제, 이동하기 용이해짐(선택 사항)
```js
const user = {
  name: 'Sophia', // 속성 1
  age: 30, // 속성 2
  'key with space': true, // 속성 3
}
```

## 2. 객체의 속성
### Property 활용
```js
// 조회(점 표기법, 대괄호 표기법)
console.log(user.age)
console.log(user['age'])
console.log(user['key with space'])

// 추가
user.address = 'korea'
console.log(user)

// 수정
user.age = 40
console.log(user)

// 삭제
delete user.address
console.log(user)
```

### Property 존재 연부 확인: `in`
```js
console.log('age' in user) // true
console.log('country' in user) // false
```

### 단축 Propery
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
```js
const age = 30
const address = 'korea'

const oldUser = {
  age: age,
  address: address,
}

const newUser = {
  age,
  address,
}
```

### 계산된 Property
- 키가 대괄호([])로 둘러싸여 있는 property
- 고정된 값이 아닌 변수 값을 사용할 수 있음
```js
const a = 'hello'
const b = 'bye'
const bag = {
  [a]: 5,
}

console.log(bag) // {hello: 5}

// 프롬프트(입력)
const product = prompt('물건 이름을 입력해주세요.')

// 연산가능
const a = 'my'
const b = 'property'
const bag = {
  [product]: 5,
  [a + b]: true,
}
```

## 3. 객체와 함수
### Method
- 객체 속성에 정의된 함수

#### object.method()
- 메서드는 객체를 **행동**할 수 있게 함
- 객체의 속성을 활용
```js
const person = {
  name: 'Sophia',
  greeting: function () {
    return 'Hello'
  },
}

// greeting 메서드 호출
console.log(person.greeting()) // Hello
```

### this 키워드
- this 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음
- 함수나 메서드를 호출한 `객체`를 가리키는 키워드(함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용)

```js
const person = {
  name: 'Sophia',
  greeting: function () {
    return `Hello, ${this.name}`
  },
}
```
- JS에서 this는 함수를 **호출하는 방법**에 따라 가리키는 대상이 다름
    1. 단순 호출 시 -> 전역 객체
    ```js
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // Window (document보다 위, 최상위 전역 객체, 생략 가능)
    ```
    2. 메서드 호출 시 -> 메서드를 호출한 객체

### Nested 함수에서의 문제점과 해결책
#### 문제점
```js
cosnt myObj2 = {
  numbers: [1, 2, 3],

  myFunc: function () {
    this.numbers.foerEach(function (num) {
      console.log(number) // 1 2 3
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc())
```
- forEach의 인자로 들어간 함수는 일반 함수 호출이기 때문에 this가 전역 객체를 가리킴

#### 해결책
```js
cosnt myObj3 = {
  numbers: [1, 2, 3],

  myFunc: function () {
    this.numbers.foerEach((num) => {
      console.log(number) // 1 2 3
      console.log(this) // myObj3
    })
  }
}
console.log(myObj3.myFunc())
```
- 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this값을 가져옴
- 메서드 정의할 떄는 화살표 함수 금지(전역 호출할 수도 있으니까~)

## 99. 참고
### 유용한 객체 메서드
```js
const profile = {
  name: 'Sophia'
  age: 30
}

console.log(Object.keys(profile)) // ['name', 'age']
console.log(Object.values(profile)) // ['Sophia', 30]
```

### JS 'this' 특징
- Js의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적)
  - 파이썬과 자바는 선언 시 값이 이미 정해짐

### JSON(Js Object Notation)
- JSON은 형식이 있는 **문자열**
  - 따라서 JS에서 쓰려면 Object로 변환해야 함.
