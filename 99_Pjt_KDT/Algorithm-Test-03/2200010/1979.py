# 1979번 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('data/1979.txt')

T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    line_cnt = 0
    column_cnt = 0


    for x in range(N):
        cnt1 = 0
        cnt2 = 0
        for y in range(N):
            
            # 행 순회
            # 1이라면
            if puzzle[x][y] == 1:
                cnt1 +=1

            # 0이라면
            elif puzzle[x][y] == 0:
                if cnt1 == K:
                    line_cnt += 1
                cnt1 = 0
            
            # 열 순회
            if puzzle[y][x] == 1:
                cnt2 += 1


            # 0이라면
            elif puzzle[y][x] == 0:
                if cnt2 == K:
                    column_cnt += 1
                cnt2 = 0
                
        if cnt1 == K: # 한 행의 최종 cnt가 K개라면 1 새어준다.   
            line_cnt += 1

        if cnt2 == K:
            column_cnt += 1

    print(f'#{t} {line_cnt + column_cnt}')
        
