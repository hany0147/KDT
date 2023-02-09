matrix = [list(map(int,input().split())) for i in range(3)]

# 행 우선
for n in matrix:
    print(*n, end =" ")

print()

# 열 우선
for x in range(3):
    for y in range(3):
        print(matrix[y][x], end = " ")

print()

# 총합
sum_n = 0
for x in range(3):
    for y in range(3):
        sum_n += matrix[x][y]
print(sum_n)

# 최댓값
max_n = 0
for x in range(3):
    for y in range(3):
        if max_n < matrix[x][y]:
            max_n = matrix[x][y]
print(max_n)

# 일차원 리스트 회전

from collections import deque
one_dim_lst = deque([1, 2, 3, 4, 5])

for i in range(5):
    one_dim_lst.appendleft(one_dim_lst.pop())
    print(*one_dim_lst)
