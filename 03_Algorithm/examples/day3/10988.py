# 10988번 팰린드롬인지 확인하기

'''
알파벳 소문자로만 이루어진 단어가 주어진다. 
이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
'''

string = input() # 알파벳 소문자로만 이루어진 단어가 주어진다. 
# 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램 -> if 문

if string[0:] == string[::-1]:
    print(1)
else:
    print(0)


#### while로 변환해서 풀어보기

while True:

    for i in range(len(string)): # 5 /  0,1,2,3,4
        if string[i] == string[len(string)-i-1]: # 0, 4 / 1, 3. 
            print(1)
        else:
            print(0)
            break
