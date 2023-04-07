# 11856번 반반
'''
길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때
S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.
'''

import sys
sys.stdin = open('data/11856.txt')

T = int(input())
for t in range(1, T + 1):
    strings = input()
    cnt = 0
    total = []
    for string1 in strings:
        for string2 in strings:
            if string1 == string2:
                cnt += 1
        total.append(cnt)
        cnt = 0
    # print(total)
    if total == [2, 2, 2, 2]:
        print(f'#{t} Yes')

    else:
        print(f'#{t} No')
        


