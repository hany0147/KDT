# A와 B가 가위바위보를 하였다.
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

# [입력]
# 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.


# [출력]
# A가 이기면 A, B가 이기면 B를 출력한다.

# import sys
# sys.stdin = open('data/input_1936.txt', 'r')

# if문 활용 (중복 심함)

a , b = list(map(int, input().split()))

if a == 1 and b == 2:
    print ('B')
elif a == 2 and b == 3:
    print('B')
elif a == 3 and b == 1:
    print('B')
elif a == 2 and b == 1:
    print('A')
elif a == 1 and b == 3:
    print('A')
elif a == 3 and b == 2:
    print('A')


# 나머지(%) 으로 구하는 법?
c , d = list(map(int, input().split()))

if (c + d) % 3 == 2:
    if c > d:
        print('A')
    else:
        print('B')
elif (c + d) % 3 == 1:
    if c > d:
        print('B')
    else:
        print('A')
elif (c + d) % 3 == 0:
    if c > d:
        print('A')
    else:
        print('B')    
