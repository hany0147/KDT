# 1251번 단어 나누기
'''
먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다.
즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다.
각각은 적어도 길이가 1 이상인 단어여야 한다. 

이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
'''
#1

words = input()
N = len(words) # arrested , N = 8
# 두 번 나눠야 한다. -> 두 번 포문을 돌린다.
# 그리고 해당 i, j가 자르는 부분이 되고, [:]로 그 범위를 설정한다.

# 두 개로 자르기.

sum_ = []
for i in range(1, N - 1):
    for j in range(i+1, N):
        word1 = words[:i]
        word2 = words[i:j]
        word3 = words[j:]
        
        r_word2 = word2[::-1]
        r_word1 = word1[::-1]
        r_word3 = word3[::-1]

        sum_.append(r_word1 + r_word2 + r_word3)

        sum_.sort()

print(sum_[0])

#########################################################################

#2

from heapq import *

word = input()
N = len(word)
sum_ = []
heapify(sum_)

for i in range(1, N-1):
    for j in range(i+1, N):
        word1 = word[:i]
        word2 = word[i:j]
        word3 = word[j:]

        r_word1 = word1[::-1]
        r_word2 = word2[::-1]
        r_word3 = word3[::-1]
 

        heappush(sum_, r_word1 + r_word2 + r_word3)

print(heappop(sum_))

###########################################################################

## 동료 코드
# word = list(input())
# result = []

# for i in range(1, len(word) - 1):
#     for j in range(i + 1, len(word)):
#         w1 = word[:i]
#         w2 = word[i:j]
#         w3 = word[j:]

#         w1.reverse()
#         w2.reverse()
#         w3.reverse()
#         result.append(''.join(w1 + w2 + w3))

# r = sorted(result)
# print(r[0])