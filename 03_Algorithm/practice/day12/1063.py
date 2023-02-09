# 1063번 킹
'''
8*8크기의 체스판에 왕이 하나 있다.

체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 
돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 

입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는
그 이동은 건너 뛰고 다음 이동을 한다.

킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.
'''
'''
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로
'''
from pprint import pprint

# 델타검색을 위한 dict
dir_dict = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

# 입력
king, stone, N = input().split()
kx, ky = 8 - int(king[1]), ord(king[0]) - 65
sx, sy = 8 - int(stone[1]), ord(stone[0]) - 65

# 체스판 초기 설정
chess = [[0]* 8 for _ in range(8)]
# pprint(chess)

# 두 체스 위치 선정
chess[kx][ky] = 1
chess[sx][sy] = 1
# pprint(chess)

N = int(N)
for _ in range(N):
    dir = dir_dict[input()] # 방향 입력
    # print(dir[0], dir[1])

    # 왕이 움직일 곳이 범위 밖인가? 그렇다면 continue
    if kx + dir[0] == 8 or kx + dir[0] == -1 or ky + dir[1] == 8 or ky + dir[1] == -1:
        continue
    else: # 아니라면
        # 해당 곳에 돌이 있는가?
        if kx + dir[0] == sx and ky + dir[1] == sy: # 있다면,
            # 돌이 움직여야 할 곳이 범위 밖인 가?
            if sx + dir[0] == 8 or sx + dir[0] == -1 or sy + dir[1] == 8 or sy + dir[1] == -1:
                continue
            else:
                chess[sx + dir[0]][sy + dir[1]] = 1
                chess[kx][ky] = 0
                kx = kx + dir[0]
                ky = ky + dir[1]
                sx = sx + dir[0]
                sy = sy + dir[1]
        else: # 돌이 없다면
            chess[kx + dir[0]][ky + dir[1]] = 1
            chess[kx][ky] = 0

            kx = kx + dir[0]
            ky = ky + dir[1]
    # pprint(chess)
 
real_kx, real_ky = str(8 - kx), chr(65 + ky)
real_sx, real_sy = str(8 - sx), chr(65 + sy)

print(real_ky + real_kx)
print(real_sy + real_sx)

    