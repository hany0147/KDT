# 0개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# 함수 활용

T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    average = round(sum(nums) / len(nums)) 
    print(f'#{t} {average}')


# for 활용

T2 = int(input())

for t2 in range(1, T2 + 1):
    sum2 = 0
    nums2 = list(map(int, input().split()))
    for num2 in nums2:
        sum2 += num2
    average2 = round(sum2 / len(nums2)) 
    print(f'#{t2} {average2}')
