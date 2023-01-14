# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

import sys
sys.stdin = open("data/input3.txt", "r")


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    for n in range(N):
        print(int(input()))

