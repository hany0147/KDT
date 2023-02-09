import sys
sys.stdin = open('data/2506.txt', 'r')

N = int(input())
checks = list(map(int, input().split()))
prev_check_num = 0
result = []
prev_sum_score = 0
# 초기값 설정.

for check_num in checks:
    score = 0 # 스코어는 매번 초기화
    if check_num == 1: # 이번 점수를 맞췄다면
        if prev_check_num == False: # 이전 점수가 틀렸다면
            score = check_num # 스코어는 1점.
            result.append(score)
            prev_sum_score = 0 # 이전 점수가 틀리다면 합친 점수 초기화
        elif prev_check_num == True: # 이전 점수가 맞았다면
            prev_sum_score += 1 # 1점씩 추가
            score = check_num + prev_sum_score # 스코어는 '이전 합친 점수' + 현 점수
            result.append(score)
    else:
        result.append(check_num)
    prev_check_num = check_num # checks의 다음 채점값이 나오기 전에 현 값이 다음 채점의 이전 채점이되기 위한 설정

# print(result) # [1, 0, 1, 2, 3, 0, 0, 1, 2, 0]

print(sum(result))

print('===================')
# while문으로 풀어보기
# 종료조건에 유의해야 함.
N = int(input())
checks = list(map(int, input().split()))

