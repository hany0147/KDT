# 9058번 더하기

T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    res = sum(nums)
    print(res)
