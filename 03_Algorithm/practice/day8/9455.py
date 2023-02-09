# 9455번 박스
'''
m행 n열로 이루어진 그리드가 주어진다.
박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다. 
모든 박스가 이동한 거리 (각 박스가 이동한 거리의 합) 을 구하는 프로그램을 작성하시오. 
'''

# 입력
'''
첫째 줄에 테스트 케이스의 개수 T
각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 
다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다.
박스가 들어있는 칸은 1로, 다른 칸은 0으로 주어진다.
각 정수 사이에는 공백이 하나 주어진다. 
'''

# import sys
# from pprint import pprint

# sys.stdin = open('data/9455.txt')
T = int(input())

for t in range(T):

    M, N = list(map(int, input().split()))
    box = [list(map(int, input().split())) for _ in range(M)]
    # pprint(box)

    # 역-열 순회
    cnt = 0

    for y in range(N):    
        for x in range(M - 1, -1, -1):

            # 0. 박스를 찾았다.
            if box[x][y] == 1:

            # 1. 박스를 이동하라.
                while True:

                    # 2. 범위 체크
                    if x + 1 == M:
                        break
                    
                    # 3. 다음이 비어있는지
                    if box[x+1][y] == 1:
                        break

                    box[x][y] = 0
                    box[x+1][y] = 1
                    cnt += 1

                    x += 1
    print(cnt)




'''
1 0 1 0 1 
0 1 0 0 0 
1 0 0 1 0
0 0 1 0 0
'''



