# 11721번 열 개씩 끊어 출력하기
'''
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 
단어의 길이가 10의 배수가 아닌 경우에는 
마지막 줄에는 10개 미만의 글자만 출력할 수도 있다.
'''

# 동료의 코드
line = input()

for i in range(len(line)): # 19개 0~18까지 반복
    print(line[i], end='') # line[0]~line[9]은 BaekjoonOn # end='' 개행을 이어붙임.(디폴트값 end='\n')
    if i%10 == 9:
        print()
    #     print() # print()의 개념을 내가 모른다. # print()은 개행의 역할을 해준다.

# 동료 코드 2

S = input()
cnt = 0

for s in S :
    cnt += 1
    for c in range(11, cnt+1, 10):
        if cnt == c :
            print()
    print(s, end = '')







# word = 'BaekjoonOnlineJudge'
# word_fin = len(word) % 10
# # print(len(strings)) # 19
# word_quot = len(word) // 10


# # # 아래의 경우는 word의 길이의 몫이 1인 경우다.
# # new_word = word[0:10] # BaekjoonOn
# # print(new_word) # BaekjoonOn
# # new_word2 = word[10:len(word)+1] # word = 'BaekjoonOn'
# # print(new_word2)

# # # 아래의 경우는 word의 길이의 몫이 2인 경우다.
# # new_word = word[0:10]
# # print(new_word)
# # new_word2 = word[10:20]
# # print(new_word2)
# # new_word3 = word[20: len(word)+1]
# # print(new_word3)

# # 따라서 for문을 돌려서 만들 수 있다.

# n = 10
# new_word = word[0+n:n]
# for i in range(word_quot + 1):
#     if len(new_word) >= 10:
#         print(new_word)
#     else:
#         new_word = word[]
    








