# 1218번 괄호 짝짓기
'''
4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.
이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.
예를 들어 아래와 같은 문자열은 유효하다고 판단할 수 있다.

'''
import sys
sys.stdin = open('data/1218.txt')

# 입력

for t in range(1, 11):
    N = int(input())
    strings = input()

    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []

# 과정

    for string in strings:
        
        if string == '(':
            stack1.append(string)
        elif string == ')':
            if stack1 != []:
                stack1.pop()
            # 스택1이 비어 않다면
            elif stack1 == []:
                break
        
        if string == '[':
            stack2.append(string)
        elif string == ']':
            if stack2 != []:
                stack2.pop()
            elif stack2 == []:
                break

        if string == '{':
            stack3.append(string)
        elif string == '}':
            if stack3 != []:
                stack3.pop()
            elif stack3 == []:
                break

        if string == '<':
            stack4.append(string)
        elif string == '>':
            if stack4 != []:
                stack4.pop()
            elif stack4 == []:
                break
        
        

    if (not stack1) and (not stack2) and (not stack3) and (not stack4):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
