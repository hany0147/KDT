# 1208번 flatten
'''
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.


가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의
# 변수 dump
<제약조건>
가로 길이는 항상 100으로 주어진다.
모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
100 * 100이다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로
그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다). 
# 조건문으로 제약 사항을 고려하라.
'''

# 입력
'''
총 10개의 테스트 케이스
1번째 줄: 덤프 횟수
그 다음 줄 : 상자의 높이값
'''
# 고려할 것
# 1. 100*100 행렬을 만들고, 행마다 상자의 높이만큼 1을 채워 넣고, 나머지는 0으로 채워 넣는다.
import sys
sys.stdin = open('data/1208.txt')
from pprint import pprint

T = 10
for t in range(1, T + 1):
    dump_num = int(input())
    grid = [[0] * 100 for _ in range(100)] # 100* 100 그리드
    # pprint(grid)
    check = list(map(int, input().split()))
    # print(check)

    # 상자 채워 넣기
    for y in range(100):
        for x in range(100 - check[y], 5):
            grid[x][y] = 1
    # pprint(grid)


    # 2. dump시키기
    dump_cnt = 0 # 덤프 횟수
    dump_dif = 0 # 높낮이 차
    highest = (0, 0) # 가장 높은 곳
    lowest = (0, 0) # 가장 낮은 곳
    while True: # 덤프 횟수가 다하거나, 평탄화 작업이 완료되면(덤프차가 0 또는 1이 되면)  break
        if dump_cnt == dump_num:
            break
        
        # 가장 높은 곳: max(check), 열의 좌표와 상관없이 행의 좌표가 가장 적은 것.
        # 행: N - max(check), 열: check[check.index(max(check))]
        highest = (100 - max(check), check.index(max(check)))
        lowest = (100 - min(check), check.index(min(check)))
        dump_dif = lowest[0] - highest[0]
        
        
        if dump_dif == 0:
            break
        else:
            # 움직이는 방법은 해당 높은 곳을 0으로 낮은 곳에 1을 채워 넣는 것.
            grid[highest[0]][highest[1]] = 0
            grid[lowest[0] - 1][lowest[1]] = 1
            dump_cnt += 1

            check[check.index(max(check))] = max(check) - 1
            check[check.index(min(check))] = min(check) + 1

            highest = (100 - max(check), check.index(max(check)))
            lowest = (100 - min(check), check.index(min(check)))
            dump_dif = lowest[0] - highest[0]
        
    print(f'#{t} {dump_dif}')        
    # pprint(grid)



