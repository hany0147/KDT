# 17608번 막대기
'''
N개의 막대기에 대한 높이 정보가 주어질 때,
오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.
'''
# 문제 접근
'''
- 오른쪽부터 왼쪽으로 순회한다.
- index -1에 해당하는 요소보다 큰 막대기를 저장한다.
- 기준 막대기는 해당 막대기로 계속 변화한다.
- 해당 리스트의 len을 확인한다.
'''

import sys
stick_num = int(input()) # 막대기 개수
sticks = [] # 막대기 리스트

for _ in range(stick_num): # 막대기 저장
    stick = int(sys.stdin.readline().rstrip()) # 막대기 입력
    sticks.append(stick) # 리스트화
# print(list(sticks))

# 막대기 순회(거꾸로)

compare_stick = sticks.pop() # 막대기 순회 기준
fin_sticks = [] # 최종 막대기 리스트
fin_sticks.append(compare_stick) # 첫번째 기준 막대기까지 삽입한다.

for stick in sticks[::-1]:

    # 기준 막대기보다 크면 최종 리스트에 삽입한다.
    if compare_stick < stick:
        fin_sticks.append(stick)
        compare_stick = stick

# print(fin_sticks)
print(len(fin_sticks))




# from collections import deque
# import sys
# stick_num = int(input()) # 막대기 개수
# sticks = deque() # 막대기 리스트

# for _ in range(stick_num): # 막대기 저장
#     stick = int(sys.stdin.readline().rstrip()) # 막대기 입력
#     sticks.append(stick) # 리스트화
# # print(list(sticks))

# # 막대기 순회(거꾸로)

# compare_stick = sticks.pop() # 막대기 순회 기준
# fin_sticks = deque() # 최종 막대기 리스트
# fin_sticks.append(compare_stick) # 첫번째 기준 막대기까지 삽입한다.

# for stick in list(sticks)[::-1]:

#     # 기준 막대기보다 크면 최종 리스트에 삽입한다.
#     if compare_stick < stick:
#         fin_sticks.append(stick)
#         compare_stick = stick

# # print(fin_sticks)
# print(len(fin_sticks))

