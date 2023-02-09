# 5576번 콘테스트
'''
두 대학에서 모두 10 명씩이 콘테스트에 참여
참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성
'''

# 입력
'''
20행으로 구성
W : 1~10
K : 11~20
0<= score <= 100
'''

W_score_lst = []
K_score_lst = []

for _ in range(1, 11):
    score = int(input())
    W_score_lst.append(score)

for _ in range(11, 21):
    score = int(input())
    K_score_lst.append(score)

W_score_lst.sort(reverse = True)
K_score_lst.sort(reverse = True)

print(sum(W_score_lst[:3]), sum(K_score_lst[:3]))


## 동료 코드

# import heapq
# import sys
# W = [int(sys.stdin.readline().strip('\n')) for _ in range(10)]
# K = [int(sys.stdin.readline().strip('\n')) for _ in range(10)]
# heapq.heapify(W)
# heapq.heapify(K)
# for _ in range(7):
#     heapq.heappop(W)
#     heapq.heappop(K)
# print(sum(W),sum(K))