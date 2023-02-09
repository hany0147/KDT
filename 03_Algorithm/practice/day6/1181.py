# 1181번 단어 정렬
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 
정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''

### sort로 푸는 방법
# 입력
N = int(input())
lst = []
for _ in range(N):
    word = input()
    if word not in lst: # 중복 방지
        lst.append(word)

lst.sort(key= lambda x : (len(x), x))

print(*lst, sep = '\n') 

    # 1. 길이가 짧은 것 / len()
    # 2. 길이가 같으면/ 사전 순(sort, 오름차순)


### 자료구조로 푸는 방법 강구 필요
# import heapq
# heapq.heappush(heap_lst, word)

## 중복 제거 -> set, dict(key 중복 x)
## dict으로 풀어보기

### 동료 풀이 방법


# import heapq

# heap = []
# N = int(input())
# for _ in range(N):
#     String = input()
#     heapq.heappush(heap,String)

# result = []
# for s in heap:
#     if s not in result:
#         heapq.heappush(result, s)

# result.sort()
# result.sort(key=len)

# print(*result, sep='\n')