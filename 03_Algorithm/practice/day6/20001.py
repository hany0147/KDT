# 20001번 고무오리 디버깅
'''
고무오리의 사용법은 다음과 같다.

"고무오리 디버깅 시작" 이라고 외친다
문제들을 풀기 시작한다
고무오리를 받으면 최근 풀던 문제를 해결한다
"고무오리 디버깅 끝" 이라고 외치면 문제풀이를 종료한다.
하지만 고무오리에는 치명적인 문제가 있는데, 
풀 문제가 없는데 사용한다면 고무오리는 벌칙으 로 두 문제를 추가한다는 점이다.
'''

# '고무오리 디버깅 끝'이 주어질 때까지 반복 -> while문
# 문제 리스트
duck = input()
question_lst = []
while True:

    answer = input()
    if answer == '문제':
        question_lst.append('문제')
    elif answer == '고무오리':
        if '문제' in question_lst:
            question_lst.pop()
        else:
            question_lst.append('문제')
            question_lst.append('문제')
    elif answer == '고무오리 디버깅 끝':
        break
        
    # 문제가 리스트 안에 있는지?
    # 없다면 문제를 리스트에 두 개 추가하라.
    # 있다면 문제를 제거하라.

# question_lst 안에 아무것도 없으면 '고무오리야 사랑해' 출력
# print(question_lst)
if len(question_lst) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')