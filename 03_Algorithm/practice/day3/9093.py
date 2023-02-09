# 9093번 단어뒤집기
'''
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.
'''
# T = int(input())

# lst = []

# for t in range(T):
#     strings = input().split() # 리스트로 반환됨
#     # print(strings) # 예시 : ['I', 'am', 'happy', 'today']

#     for string in strings: # string의 타입은 문자열
#         rev_str = string[::-1] # string을 뒤집는다. reversed() 함수는 리스트의 내장함수다.
  
#         lst.append(rev_str)

#     print(*lst)

#     ## 출력초과 뜸

T = int(input())

for t in range(T):
    strings = input().split()
    sort_str = [strings[i][::-1] for i in range(len(strings))]
    print(*sort_str, sep=" ")
