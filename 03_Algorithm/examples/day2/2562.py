# 2562번 최댓값

num_list = []

for n in range(9):
    num = int(input())
    num_list.append(num)


max_num = max(num_list)
print(max_num, num_list.index(max_num) + 1, sep = '\n')



print('======================')

# list comprehension으로 풀어보기

