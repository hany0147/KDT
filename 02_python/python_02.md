# 파이썬 2일차
## 1. String Formatting
### String Interpolation
- `f-string`
```python
name = 'Jang Hanui'
evaluation = '최고'

print(f'{name}는 {evaluation}다.')

# Jang Hanui는 최고다.
```

## 2. 형 변환
### 자료형 변환
- 암시적 형 변환
  - bool(True/False)
  - numeric type(int, float, complex)
- 명시적 형 변환
  - int, float, comples, list 등등 모두 `str`로 변환 가능.
  - 숫자 형식의 str은 int나 float으로 변환 가능.

## 3. 제어문
기본적으로 위에서 아래로 `순차적`으로 명령을 수행함.
### 조건문(Conditional Statement)

- 기본 조건문
```python
if <expression>:
    # Run this Code block
else:
    # Run this Code block
```

- 복수 조건문
```python
if <expression>:
    # Run this Code block
elif <expression>:
    # Run this Code block
else:
    # Run this Code block
```
> `else`는 나머지 모든 상황을 의미하기 때문에 `조건을 달면 오류`가 난다.

-중첩 조건문
```python
if <exp>:
    # Code Block
    if <exp>:
      # Code Block
else:
    # Code Block
```

### 레인지(Range)
- 숫자의 시퀀스를 나타내기 위해 사용한다.
- 변경 불가능, 반복 가능
- 수가 많을 때 사용하기 용이함(list는 메모리를 많이 잡아 먹는다.)

- range(n): 0부터 n-1
- range(n, m): n부터 m-1
- range(n, m, s): n부터 m-1까지 s만큼 증가시켜서

### 반복문(Loop Statement)
- For문: 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함.
```python
for <변수명> in <iterable>:
    # Code block
```
>`end = " "`를 쓰면 한 줄로 나열됨

> `len()`: 해당 문자열의 길이

- 반복문 제어
  - break: 종료
  - continue: continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행.
  - for-else: 끝까지 반복문을 실행한 이후에 else문 실행

  ---
  ---
  

- [Python tutor](https://pythontutor.com/python-debugger.html#mode=edit) : 파이썬 코드를 시각화하여 이해에 도움을 주는 사이트