# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.

import sys
sys.stdin = open("data/input9.txt", "r")

T, N = list(map(int, input().split()))

for t in range(1, T + 1):
    for n in range(N):
        nums = list(map(int, input().split()))
        print(*nums)