# 9076번 점수 집계
'''
이전에는 5명의 심판이 1점부터 10점까지 정수의 점수를 주면
최고점과 최저점을 하나씩 제외한 점수의 합을 총점으로 하였다.

이를 보완하기 위해

최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면
점수 조정을 거쳐서 다시 점수를 매기려고 한다.

점수를 집계하여 총점을 계산하거나, 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에는
총점 대신 KIN(Keep In Negotiation)을 출력하는 프로그램을 작성하시오.
'''

# 입력
'''
각 테스트 케이스에 대해서 총점을 한 줄씩 출력
만일 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에는 총점 대신 KIN을 출력
'''

T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))
    # 0. 기존처럼 최고점, 최저점을 리스트에서 제외하라.

    scores.sort() # 최고점이 오른쪽
    scores.pop() # 최고점 제거
    scores.pop(0) # 최저점 제거
    # print(scores)

    # 1. 점수를 조정할 필요가 없으면(즉, 나머지 3명의 최고점 최저점 차가 4점 미만이면) -> 이전 방식으로 출력
    
    if scores[2] - scores[0] < 4:
        print(sum(scores))

    # 2. 점수를 조정해야 한다면(즉, 나머지 3명의 최고점 최저점 차가 4점 이상이면) -> KIN 출력
    else:
        print('KIN')


## 동료 코드
# T = int(input())
# for i in range(T):
#     n = list(map(int,input().split()))
#     n.remove(max(n))
#     n.remove(min(n))
#     if max(n) - min(n) >=4:
#         print('KIN')
#     else:
#         print(sum(n))