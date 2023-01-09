# 파일 입출력
```python
Open(file, mode = 'r', endcoding = none)
```
- file: 파일명
  - 해당 파일의 경로를 확인해야 한다.
- mode: 텍스트 모드
  - r(deafault) = 읽기 모드
  - a = 처음부터 쓰기 
  - w = 그 다음부터 쓰기

## 파일 활용
```python
파일 객체 활용
f = open('workfile', 'w', encoding = UTF-8)
  - 한글일 경우, UTF-8

with 키워드 활용
with open('workfile', 'w', encoding = UTF-8) as f:
  read_data = f.read()
```
> with 키워드를 사용하지 않는다면, `f.close()`를 반드시 호출하여 종료하여야 오류가 발생하지 않는다. 그러니까 그냥 `with` 키워드를 쓰라.

## JSON
- 개발환경에서 많이 활용되는 데이터 양식
- 웹 어플리케이션에서 데이터 전송할 때 사용

## 활용

```python
import json
x = json.load(f)
```

## pprint
- 파이썬 데이터 구조를 정갈하게 인쇄할 수 있는 기능
```python
from pprint import pprint
pprint()
```
