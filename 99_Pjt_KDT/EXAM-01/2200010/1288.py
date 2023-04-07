# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.

# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며
#  1부터 시작한다)를 출력하고,
# 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서
#  0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
# ( 민석이는 xN번 양을 세고 있다. )

# import sys
# sys.stdin = open('data/새로운 불면증 치료법.txt', 'r')

# SWEA 1288번 새로운 불명증 치료법
'''
N의 배수 번호인 양을 세기로 하였다.
이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
'''

# 0~9까지 모든 숫자가 나올 떄의 CNT

T = int(input())
for t in range(1, T + 1):
    N = int(input()) # 입력값
    cnt = 1 # 양 세기
    n_set = set()
    while True: # 0부터 9가 나올 때까지
        strings = str(N * cnt)
        for string in strings:
            n_set.add(int(string))
            # print(n_set)

        if n_set == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
            break

        else:
            cnt += 1

    print(f'#{t} {cnt * N}')
