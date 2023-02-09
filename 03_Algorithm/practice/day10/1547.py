# 1547번 공
'''
컵의 번호는 맨 왼쪽 컵부터 순서대로 1번, 2번 3번
먼저 1번 컵의 아래에 공을 하나 넣는다. 세준이는 두 컵을 고른 다음, 그 위치를 맞바꾸려고 한다.

예를 들어, 고른 컵이 1번과 2번이라면, 1번 컵이 있던 위치에 2번 컵을 이동시키고,
동시에 2번 컵이 있던 위치에 1번 컵을 이동시켜야 한다.
이때 공은 움직이지 않기 때문에, 공의 위치는 맨 처음 1번 컵이 있던 위치와 같다.

세준이는 컵의 위치를 총 M번 바꿀 것이며, 컵의 위치를 바꾼 방법이 입력으로 주어진다.
위치를 M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하는 프로그램을 작성하시오.
'''

# 먼저 1번 컵에 넣는다.
# 인덱스 0에 무조건 공이 있으니 인덱스 0을 출력하라.

# 입력
M = int(input()) # 컵의 위치를 바꾼 횟수 (<= 50)

ball_dict = {
    '1' : 1,
    '2' : 0,
    '3' : 0,
}

for _ in range(M):
    X, Y = input().split()
# 해당 자리에 공이 있으면, 바꾼 곳에 공을 주고, 기존은 0으로 설정한다.
    if ball_dict[X] == 1:
        ball_dict[Y] = 1
        ball_dict[X] = 0
# 만약 해당 자리에 공이 없고, 바꿀 자리에 공이 있다면, 
    elif ball_dict[Y] == 1:
        ball_dict[X] = 1
        ball_dict[Y] = 0
        
    
# 바꾼 자리에 공이 없으면, -1 출력
if 1 not in ball_dict.values():
    print(-1)
else:
    for i in range(1, 4):
        if ball_dict[str(i)] == 1:
            print(i)


## 동료 코드 1
# n = int(input())
# cup = 1
# error = -1
# for i in range(n):
#     x,y = map(int,input().split())
#     if x and y not in [1,2,3]:
#         print(cup = error)
#         break
#     if x == cup:
#         cup = y
#     elif y == cup:
#         cup = x
# print(cup)

## 동료 코드 2
# T = int(input())
# # T = int(4)
# A = 1
# for test_case in range(T):
#     n, m = map(int, input().split())
#     if n == A:
#         A = m
#     elif m == A:
#         A = n
# print(A)