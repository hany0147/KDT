# 2001번 파리퇴치

'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

<제약 사항>
1. 5<= N <= 15
2. 2<= M <= 15
3. 각 영역 파리 개수 <= 30
'''

import sys
sys.stdin = open('data/2001.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = list(map(int, input().split())) # N: 배열 수, M: 파리채 크기 
    grid = [list(map(int, input().split())) for _ in range(N)] # 파리의 나열

    # M 값의 가동 범위(N - M + 1)
    max_kill = 0

    for x in range(N - M + 1):
        for y in range(N - M + 1):
            fly_sum = 0
            for fx in range(x, x + M):
                for fy in range(y, y + M):
                    fly_sum += grid[fx][fy]

            if max_kill < fly_sum:
                max_kill = fly_sum
    print(f'#{t} {max_kill}')



        

