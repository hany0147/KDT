# 2576번 홀수
'''
7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고,
 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 
그 합은 77 + 41 + 53 + 85 = 256이 되고,

41 < 53 < 77 < 85 이므로 홀수들 중 최솟값은 41이 된다.
'''

num_lst = []
sum_num = 0
min_num_lst = []

for i in range(7):
    num = int(input())
    num_lst.append(num)

# print(num_list) # [12, 77, 38, 41, 53, 92, 85]

for num in num_lst:
    if num % 2 == 1:
        sum_num += num
        min_num_lst.append(num)
        
if sum_num == 0:
    print(-1)
else:
    print(sum_num, min(min_num_lst), sep = '\n')

