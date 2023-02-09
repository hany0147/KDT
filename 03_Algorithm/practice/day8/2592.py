# 2592번 대표값
'''
열 개의 자연수가 주어질 때 이들의 평균과 최빈값을 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다.
주어지는 자연수는 1,000 보다 작은 10의 배수이다.
'''

# 출력
'''
첫째 줄에는 평균을 출력하고, 둘째 줄에는 최빈값을 출력한다.
최빈값이 둘 이상일 경우 그 중 하나만 출력한다. 평균과 최빈값은 모두 자연수이다.
'''
import sys

sys.stdin = open('data/2592.txt')

freq_dict = {}
sum_num = 0

for i in range(10):
    num = int(input())
    sum_num += num
    if num not in freq_dict:
        freq_dict[num] = 1
    else:
        freq_dict[num] += 1

print(int(sum_num / 10))

freq_lst = []
for key, value in freq_dict.items():
    freq_lst.append((key, value))
freq_lst.sort(key = lambda x : x[1], reverse = True)
print(freq_lst[0][0])



## 동료 코드
# n_list = []

# for i in range(10):
#     num = int(input())
#     n_list.append(num)
   
# average = int(sum(n_list) / 10)
# m_num = max(n_list, key = n_list.count)

# print(average)
# print(m_num)