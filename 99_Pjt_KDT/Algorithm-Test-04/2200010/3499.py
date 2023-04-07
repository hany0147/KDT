# 3499번 퍼펙트 셔플
'''
카드를 퍼펙트 셔플 한다는 것은, 
카드 덱을 정확히 절반으로 나누고 
나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다. 

N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성

만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.
'''

import sys
sys.stdin = open('data/3499.txt')

T = int(input())

for t in range(1, T + 1):

    N = int(input())
    deck = input().split()
    perfect_deck = []
    # print(deck)
    if N % 2 == 0:
        for n in range(round(N/2)):
            perfect_deck.append(deck[n])
            perfect_deck.append(deck[n + round(N/2)])

    elif N % 2 == 1:
        for n in range(round((N//2) + 1)):
            perfect_deck.append(deck[n])

            if n == round(N//2):
                break
            else:
                perfect_deck.append(deck[n + round(N//2) + 1])

    print(f'#{t}', *perfect_deck)
