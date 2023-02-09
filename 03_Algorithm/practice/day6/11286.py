# 11286번 절댓값 힙
'''
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

# 입력
# 입력되는 정수는 -2**31보다 크고, 2**31보다 작다.
# -> 수가 크므로 단순 리스트 자료 구조로 해결하면 안 됨.
import sys
# sys.stdin = open('11286.txt', 'r')

import heapq

N = int(sys.stdin.readline())
num_lst = []

for _ in range(N):
    x = int(sys.stdin.readline())
    # abs_x = abs(x)  # 절댓값: abs(x)

    # 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
    if x != 0:
        heapq.heappush(num_lst, (abs(x), x))
        
    # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
    # 가장 작은 값 -> heap 구조 (min) / heappush(heap, item), heappop(heap)

    # 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
    else:
        if num_lst:
            # num_lst.sort(key = lambda x :(x, x[1])) 이거 필요 없어. print 다시 해봐서 비교해보자.
            # lambda의 원리 공부 필요
            print(heapq.heappop(num_lst)[1])
        else:
            # 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
            print(0) 

### 동료 코드

# import sys
# import heapq

# abs_heap = []

# n = int(sys.stdin.readline())
# for i in range(n):
#     num = int(sys.stdin.readline())
#     if num:
#         heapq.heappush(abs_heap, (abs(num), num))
#     else:
#         if abs_heap:
#             print(heapq.heappop(abs_heap)[1])
#         else:
#             print(0)




