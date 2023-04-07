# 3456번 직사각형 길이 찾기

'''
직사각형의 네 변 중에서 세 변의 길이가 주어진다.

나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.
세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.

입력으로 직사각형이 불가능한 경우는 주어지지 않는다.

다음 그림의 예시는 각각 a = 4, b = 3, c = 4의 입력과 a = 5, b = 5, c = 5의 입력을 받았을 때 직사각형의 모습이다.
빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.
'''

import sys

sys.stdin = open('data/3456.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    a, b, c = list(map(int, input().split()))
    if a == b == c:
        print(f'#{t} {a}')
    elif a == b and a != c:
        print(f'#{t} {c}')
    elif a == c and a != b:
        print(f'#{t} {b}')
    elif b == c and a != b:
        print(f'#{t} {a}')