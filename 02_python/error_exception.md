# 에러/예외 처리(Error/Exception Handling)
## 디버깅
- branches: 모든 조건이 원하는대로 동작하는지?
- for loops: 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops: 종료 조건이 제대로 동작하는 지
- function: 함수 호출시, 함수 파라미터, 함수 결과

## 문법 에러(Syntax Error)
- EOL(End of Line), EOF(End of File)
- Invalid syntax
- assign to literal

## 예외(Exception)
- 실행 중에 감지되는 에러
1. ZeroDivisionError: 0으로 나누고자 할 때 발생
```python
10/0
```
2. NameError: namespace 상에 이름이 없는 경우
3. `TypeError`: 타입 불일치
```python
1 + '1'
round('3.5')
```
  - arguments 부족, argument 개수 초과
4. ValueError: 타입은 올바르나 값이 적절하지 않거나 없는 경우
5. IndexError
6. KeyError
7. ModuleNotFoundError: 존재하지 않는 모듈을 import하는 경우
8. ImportError: 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
9. IndentationError: Indentation(들여쓰기)이 적절하지 않는 경우
10. KeyboardInterrupt: 임의로 프로그램을 종료하였을 때

## 예외 처리
try 문 / except 절을 이용하여 예외 처리 가능
- try문: 오류 발생 가능성있는 코드 실행. 예외 발생하지 않으면 except 없이 실행 종료
- except절: 예외 발생하면, except절 실행
- try문은 반드시 한 개 이상의 except문이 필요
```python
try:
  <오류 뜰 수 있는 코드>
except:
  <조치할 코드>
```