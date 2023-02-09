# 1652번 누울 자리를 찾아라
'''
NxN의 정사각형모양
 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 
 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 

<조건>
1. 똑바로 연속해서 2칸 이상의 빈 칸이 존재
2. 가로로 누울 수도 있고 세로로 누울 수도 있다.
3. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다
    (중간에 어정쩡하게 눕는 경우가 없다.)
'''

# 입력
'''
첫째 줄에 방의 크기 N이 주어진다. N은 1이상 100이하의 정수이다.
그 다음 N줄에 걸쳐 N개의 문자가 들어오는데 '.'은 아무것도 없는 곳을 의미하고,
'X'는 짐이 있는 곳을 의미한다.
'''

# 출력
'''
가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력한다.
'''
## 첫 번쨰 방법: 틀렸다고 뜸 (문제를 잘 못 이해한 것 같다.)

# .. 이 연속으로 두 개 존재해야 함. 
# 그런 행과 열은 1자리로 카운트
# 따라서 행과 열을 각각 순회하면서 가로 세로 누울 자리를 카운팅 해야한다.

# import sys
# import copy

# sys.stdin = open('data/1652.txt')

# # 1. 메트릭스 생성
# from pprint import pprint

# matrix = []
# N = int(input())
# for _ in range(N):
#     strings = input()
#     lst = []
#     for string in strings:
#         lst.append(string)
#     matrix.append(lst)

# # pprint(matrix)

# # 2. 행 순회
#   # .. 이 연속으로 두 개 존재해야 함.  이걸 어떻게 표현하지?
# line_cnt = 0
# new_matrix = copy.deepcopy(matrix)
# for x in range(len(new_matrix)):
#     string = ''
#     while new_matrix[x] != []:
#         string += new_matrix[x].pop()
#     if '..' in string:
#         line_cnt += 1

# # 3. 열 순회
# column_cnt = 0
# column_lst = []
# for x in range(len(matrix)):
#     for y in range(len(matrix[0])):
#         column_lst.append(matrix[y][x])
#     string = ''
#     while column_lst != []:
#         string += column_lst.pop()
#     if '..' in string:
#         column_cnt += 1

# print(line_cnt, column_cnt)

## 두 번째 방법
import sys
sys.stdin = open('data/1652.txt')

# 쭉 뻗어 눕는다는 것이 위 아래가 짐이든 벽이든 막혀 있어야 한다는 뜻
# 조건
# (1) ..이 연속으로 2이상 있어야 한다. 2이상 있을 경우 자리를 +1 카운팅한다.
# (2) x로 막히면 리셋하여 다시 ..을 카운팅한다.
# (3) 행렬 순으로 카운팅한다.

# 1. 입력 생성(유사 행렬)

N =  int(input())
room = [input() for _ in range(N)]
# print(room) # ['....X', '..XX.', '.....', '.XX..', 'X....'] 
# print(room[0][0]) # .

# 2. 행 / 열 순회
    # room[x][y] 행 순회
    # room[y][x] 열 순회

line_result = 0
column_result = 0

for x in range(N):

    line_cnt = 0
    column_cnt = 0

    for y in range(N):

        if room[x][y] == '.':
            line_cnt += 1
            if line_cnt == 2:
                line_result += 1
        else:
            line_cnt = 0

        if room[y][x] == '.':
            column_cnt += 1
            if column_cnt == 2:
                column_result += 1
        else:
            column_cnt = 0

print(line_result, column_result)
                

## 동료 코드


# n = int(input())
# condo = [input() for _ in range(n)]
# count1, count2 = 0,0
# for i in range(n):
#     cnt_1,cnt_2 = 0,0
#     for j in range(n):
#         if condo[i][j] == '.':
#             cnt_1 +=1
#             if cnt_1 == 2:
#                 count1 +=1
#         elif condo[i][j] != '.':
#             cnt_1 = 0

#         if condo[j][i] == '.':
#             cnt_2 +=1
#             if cnt_2 == 2:
#                 count2 +=1
#         elif condo[j][i] != '.':
#             cnt_2 = 0

# print(count1, count2)

#..X..
