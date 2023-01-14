# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

# 단, 주어질 숫자는 10000을 넘지 않는다.

import sys
sys.stdin = open("data/input_2025.txt", "r")

nums = int(input())
result = 0
for num in range(1, nums + 1):
    result += num

print(result)