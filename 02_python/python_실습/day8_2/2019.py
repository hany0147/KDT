# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.


import sys
sys.stdin = open('data/input_2019.txt', 'r')

N = int(input())
num_list = []


for n in range(0, N + 1):
    num = 2**n
    num_list.append(num)

print(*num_list)