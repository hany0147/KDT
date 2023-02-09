# 2750번 수 정렬하기

N = int(input())
n_list = []
for n in range(N):
    num = int(input())
    n_list.append(num)

n_list.sort()


print(*n_list, sep = '\n')