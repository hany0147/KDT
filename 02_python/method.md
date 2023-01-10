# 메서드

## 문자열
### 탐색/검증
- s.find(x): x의 첫 번째 위치를 반환. 없으면 -1을 반환
- s.index(x): x의 첫번째 위치를 반환. 없으면 오류 발생.
- s.`is`~: boolean 값을 반환.

### 변경
- s.replace(old, new[, count]): 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
- s.strip([chars]): 공백이나 특정 문자를 제거
- s.split(sep=None, maxsplit=-1): 공백이나 특정 문자를 기준으로 분리