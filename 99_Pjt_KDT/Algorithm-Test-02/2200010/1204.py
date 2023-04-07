# 1204번 1일차 - 최빈수 구하기

'''
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
'''


import sys

sys.stdin = open('data/1204.txt', 'r')

# runtime error 떴으므로 다른 방법을 찾아보자 ^^

# import statistics

# T = int(input())

# for t in range(1, T + 1):
#     test = int(input())
#     scores = list(map(int, input().split()))

#     most_freq_score =  max(statistics.multimode(scores))

#     print(f'#{test} {most_freq_score}')


T = int(input())

for t in range(1, T + 1):
    test = int(input())
    scores = list(map(int, input().split()))
    compare_score = 0
    lst = []

    for n in range(0, 101):
        freq_score = scores.count(n)
        if compare_score <= freq_score:
            compare_score = freq_score
            lst.append(n)

            
    print(f'#{test} {lst[-1]}')

    # 강사님의 풀이 방식 : dict, dict.items()





    
    
