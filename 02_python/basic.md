# 파이썬의 기초
컴퓨터 프로그래밍 언어란?: 
컴퓨터에게 명령하기 위한 약속
- `컴퓨터`는 저장하고 조작하는 기기
- `프로그래밍`은 명령어의 모음
- `언어`는 자신의 생각을 나타내고 전달하기 위해 사용하는 체계.

## 파이썬의 특징
- easy to learn
- 인터프리터 언어
- 객체 지향 프로그래밍

## 객체와 변수
- `객체`: ~한 것(물건) / 파이썬에 담길 모든 것(숫자, 문자, 클래스 등)
- `변수`: 객체를 참조하기 위해 사용되는 이름. 다른 객체를 언제든 할당 할 수 있기 때문에 `변수`라 불림.
  - `연산자(=)`을 통해 할당.
  - ㅇ <- ㅁ
  - 오른쪽의 값을 왼쪽에 `할당`.
> `type()`을 통해 수시로 해당 객체의 유형을 확인하는 게 중요.
- 같은 값 동시 할당 가능.
```python
x = y = 100
```
- 다른 값 동시 할당 가능.
```python
x, y, = 1, 2
```

### 식별자
- 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는 데 쓰는 이름
- `예약어` 사용 불가
- 숫자, 영어 알파벳(대소 구분함), 언더스코어(_)로 구성

### 자료형
`객체의 종류 = 타입(type)`

1. 숫자
  1. 수치형
      - int, float, complex
      - `not iterable`
  2. 불린형
      - True / False (1 / 0)
  3. 컨테이너
  - 여러개의 값을 담을 수 있는 객체
     1. 시퀀스(iterable)
      - 문자열: '' or ""로 표기, 인덱싱으로 접근가능, `immutable`
      ```python
      s[1] = 'b'
      a, b, c, d, e, ...
      ```
      ```python
      슬라이싱(마지막 숫자 이전까지)
      s[2:5] = 'cde'
       a, b, c, d, e, ...
      ```
      ```python
      결합
      'hello' + 'world'
      # hello, world

      반복
      'hi' * 3
      # hihihi

      포함

      'a' in 'apple'
      # True

      Escape sequence
      \n : 줄바꿈
      \t : 탭
      ```
      
      - 리스트: 순서 존재, 서로 다른 타입 가능, `[]`으로 이뤄짐, `mutable`, 인덱스 가능
      ```python
      값 추가 : .append(값)
      값 삭제 : .pop(인덱스)
      ```

      - 튜플: `불변`한 값들의 나열. 순서 있으며, 서로 다른 타입의 요소 가질 수 있음. `immutable`. ()로 정의. tuple()로 생성 가능. 값 접근은 인덱스로 가능하나, 추가는 불가.

      - 레인지: `숫자의 시퀀스`, `immutable`, 수가 많을 때 사용하기 용이(lists는 메모리를 많이 잡아 먹음.)
      ```python
      range(n): 0부터 n-1
      range(n, m): n부터 m-1
      range(n, m, s): n부터 m-1까지 s만큼 증가시켜서
      list(range(n)): 담겨 있는 숫자를 확인하기 위해선 리스트로 형변환 필요.
      
      # 역순
      range(n, m, -1)
      ```

  4. 컬렉션
    1. 딕셔너리(Dictionary)
    - `키-값(key-value)` 쌍으로 이루어진 모음
    - `{}`
    - `:`으로 구분. 개별 요소는 `,`으로 구분.
    - `mutable`
    - `키는 immutable한 데이터`만 활용가능(string, int, float, boolean, tuple, range)
    - `값은 모두` 설정 가능(list, dictionary 등)
    ```python
    키와 값의 쌍 추가
    x['name'] = '홍길동'

    키 삭제
    x.pop('name')
    
    키가 없는 경우 KeyError 발생
    ```
    - 기본적으로 `key를 순회`함.
    
    2. 세트(Set)
    - `유일`한 값들의 모음
    - `순서가 없고`, `중복된 값이 없음` 
    - `mutable`
    - {} 혹은 set()
    - 인덱싱 불가
    - 값 추가: .add(값)
    - 값 삭제: .remove(값)




  5. None
      - 일반적으로 반환 값이 없을 때 사용.


----
----
### 연산자
- 산술 연산자
> +(더하기), -(빼기), *(곱하기), /(나누기), //(몫), %(나머지), **(거듭제곱)

- 비교 연산자: !=(아니다), ==(같다)

- 논리 연산자: 참 and 참(참), 참 and 거짓(거짓), 거짓 and 거짓(거짓)

## 기타

### 주석
- `#` 사용하면 되며, `ctrl + /`를 하면 해당 줄이 주석이 됨.

### 사용자 입출력
- input(): 사용자로 부터 값을 입력 받는 내장 함수
> `반환값은 항상 문자열로 변환`되므로 int()를 활용해야할 때가 있음.
- print(): 결과물 출력
> print()를 수시로 하여 출력값을 예상할 수 있어야 함.

---
---


## 형변환
### String Formatting
- `f-string`
```python
name = 'Jang Hanui'
evaluation = '최고'

print(f'{name}는 {evaluation}다.')

# Jang Hanui는 최고다.
```

### 형 변환
#### 자료형 변환
- 암시적 형 변환
  - bool(True/False)
  - numeric type(int, float, complex)
- 명시적 형 변환
  - int, float, comples, list 등등 모두 `str`로 변환 가능.
  - 숫자 형식의 str은 int나 float으로 변환 가능.

---
---
- [Python tutor](https://pythontutor.com/python-debugger.html#mode=edit) : 파이썬 코드를 시각화하여 이해에 도움을 주는 사이트