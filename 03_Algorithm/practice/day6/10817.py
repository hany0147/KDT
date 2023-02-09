# 10817번 세 수
'''
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
'''

# sort 함수를 써서 인덱스로 뽑아내기

nums = list(map(int, input().split()))

nums.sort(reverse = True)

print(nums[1])


### 동료 코드

# import heapq
# N = list(map(int, input().split()))
# heap = []
# heapq.heapify(N)
# heapq.heappop(N)
# print(heapq.heappop(N))