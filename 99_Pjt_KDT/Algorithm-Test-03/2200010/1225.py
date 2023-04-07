# 1225번 암호생성기
'''
<1 사이클>
8개의 숫자 입력받기
첫 번째 숫자 -1, 맨 뒤로 보내기
그 다음 첫번째 수는 -2, 맨뒤로 보내기
그 다음 -3 맨뒤로 
-4
-5
-------
숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되고 프로그램 종료
'''

import sys
sys.stdin = open('data/1225.txt')

for _ in range(10):
    T = int(input())
    nums = list(map(int, input().split()))

    while True: # 음수가 나올 때까지 돌려
        
        for n in range(1, 6):
            new_num = nums.pop(0) - n
            if new_num <= 0:
                nums.append(0)
                break
            else:
                nums.append(new_num)

        if nums[-1] == 0:
                
            break

    print(f'#{T}', end = " ")

    for num in nums:
        print(num, end = " ")

    print()