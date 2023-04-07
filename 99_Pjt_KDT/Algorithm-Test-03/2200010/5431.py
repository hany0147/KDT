# 5431번 민석이 과제 체크하기
'''
수강생들은 1번에서 N번까지 번호가 매겨져 있고,
어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.
'''
# 입력
'''
1번째 줄
N: 수강생의 수를 나타내는 정수(2≤N≤100)
K: 과제를 제출한 사람의 수를 나타내는 정수(1≤K≤N)

2번째 줄
과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 
'''
T = int(input()) # 2

for t in range(1, T + 1):
    
    N, K =list(map(int, input().split()))
    pass_lst = list(map(int, input().split()))
    fail_lst = []

    # 제출한 사람 리스트 pass_lst = []
    # pass_lst에 포함되어 있지 않은 사람을 뽑아내는 문제
    # 오름차순이므로 sorted로 변환

    for student in range(1, N + 1):
        if student not in pass_lst:
            fail_lst.append(student)

    fin_lst = sorted(fail_lst)
    lst = ''
    print(f'#{t}', end = " ")
    for i in fin_lst:
        
        print(str(i), end = " ")

    print()

    