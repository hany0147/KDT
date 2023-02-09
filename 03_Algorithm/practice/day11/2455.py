# 2455번 지능형 기차
'''
출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산
단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여,
역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.

1. 기차는 역 번호 순서대로 운행한다.
2. 출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0이다.
3. 각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
4. 기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다.

기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.
'''

# train_in, train_out, total
# 먼저 내리고 탄다.

total = 0
lst = []
for _ in range(4):
    train_out, train_in = list(map(int, input().split()))
    total = total - train_out + train_in
    # print(f'#{_}: {total}')
    lst.append(total)

print(max(lst))