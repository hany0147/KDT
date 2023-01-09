# 함수(Fuction)
`input -> output`

`함수도` 그 자체로 `객체`이다. 

Why use?
- abstraction(추상): 가독성, 생산성, 재사용성
- decomposion(분해): 기능 분해
- 코드 중복 방지, 재사용 용이함

## 내장 함수
- 구글에 '파이썬 내장함수' 검색하면 나옴
> ex) print(), len(), sum(), max(), min(), abs(x), divmod(a, b), sorted() 등등
- `map(function, iterable)`
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수 적용하고, 그 결과를 map object로 반환
```python
numbers = list(map(int, input().split()))
```


- `중요한 것은 함수의 설명을 이해하는 것!`
  - iterable: 반복가능한 모든 객체(리스트, 문자열 등등)

```python
  print(*objects, sep=' ', end='\n', file=None, flush=False)
  - *object: *은 여러값을 무한하게 받을 수 있음을 의미.
  - sep=' ': sep라는 키워드는 기본 값이 space
  - end='\n': end라는 키워드는 기본 값이 개행 
 ```
