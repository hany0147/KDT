# 사용자 정의 함수
## 선언과 호출
- `def`
- 들여쓰기를 통해 function body를 작성
- 함수명()으로 호출
```python
def func1(a, b):
  return a + b
```
## 함수의 결과값(output)
- 함수는 반드시 값을 하나만 return
- 명시적인 return문이 없는 경우: `none` 반환
- 여러 값을 return 하는 경우: `tuple` 반환.
- 하나의 return 이후 함수 정의 종료됨.

return vs print
- return: 함수 안에서 값을 반환하기 위해 사용되는 **키워드**
- print: 출력을 위해 사용되는 **함수**

## 함수의 입력(input)
- Parameter: 함수 내부에서 사용되는 식별자
- Argument: 함수를 호출할 때, 넣어주는 값
  - 필수 argument: 반드시 전달되어야 하는
  - 선택 argument: 값 전달하지 않아도 되는 경우는 기본 값이 전달
  - positional argument: 기본은 위치로 인자를 받음.
  - keyword argument: 키워드로 호출. 
  - default arguments values: 기본값을 지정하여 함수 호출(정의된 것보다 더 적은 개수의 argument들로 호출 될 수 있음)
  - 정해지지 않은 개수의 argument: `*`(튜플로 묶임)
    - 몇 개의 positional argument를 받을지 모르는 함수 정의에 유용
  - 정해지지 않은 개수의 keyword argumentsL: `**`, 딕셔너리로 묶여 처리됨.

  ## 함수의 범위(scope)
  > 객체는 각자의 수명주기가 존재함
  - bulit in scope: 영원히 유지
  - global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
  ### 이름 검색 규칙(Name Resolution)
  **LEGB 규칙**
  > Local - Enclosed - Global - Built-in

  