# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.

import sys
sys.stdin = open("data/input5.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    for n in range(N):
        print(input())