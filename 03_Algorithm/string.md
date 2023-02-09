# 문자열
`immutable` 자료형

## 문자열 조작

### 슬라이싱
- start: 이상
- end: 미만
> 예시: s[2:5] / s[-6:-2] -> 2이상 5미만, -6이상 -2미만
- step
> 예시: s[2:5:2] -> 2이상 5미만 2단계씩
> 예시: s[2:5:-1] -> 2이상 5미만으로 가야하는데 -1로 가라하면 `''`으로 도출됨. 정상적으로 가려면 s[5:2:-1] 해야 함.
- start와 end는 생략 가능
> 예시: s[:3] -> 시작부터 3미만까지, s[5:] -> 5이상부터 끝까지
- 왜 len()을 쓰지? 복습 필요
> s[::-1] -> 역순


정규 표현식(re): 문자열의 패턴일치 관련에서 문제풀이 할 때 쉽게 할 수 있음.

## 메서드
1. .split(기준 문자): 문자열을 일정 **기준**으로 나누어 **리스트**로 반환
2. .strip(제거할 문자): 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환
3. .find(찾는 문자): 위치(인덱스)를 반환. 찾는 문자가 없다면 -1을 반환
4. .index(찾는 문자): 위치(인덱스)를 반환. 없으면 오류.
5. .count(개수를 셀 문자): 특정 문자가 몇 개인지 반환. 문자열의 개수도 가능
6. .replace(기존 문자, 새로운 문자): **수정**한 새로운 문자열 반환, 특정 문자를 ""로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능
    - 단순 순회로 문제를 푸는 게 더 쉬울 수 있다.
7. 삽입할 문자.join(iterable):
8. .startwith('문자'): 특정 문자열로 시작하는 지?
9. .endswith('문자'): 특정 문자열로 끝나는 지?

## 아스키(ASCII) 코드
- 알파벳을 표현하는 대표 인코딩 방식
1. ord(문자): 문자 -> 아스키코드로 변환하는 내장함수
2. chr(아스키코드): 아스키코드 -> 문자로 변환하는 내장함수