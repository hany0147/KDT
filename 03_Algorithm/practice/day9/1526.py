# 1526번 가장 큰 금민수
'''
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다
금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성
'''

# 입력
'''
첫째 줄에 N이 주어진다.
N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.
'''

# 문자열 접근
# 1. 문자열로 바꾸어 '4' 또는 '7'이 포함되어 있는지 여부를 확인하고
# 2. 이를 다시 int로 형변환 하여 max 값을 구현한다. 이 max값은 <= N 이다.

N = int(input())
max_n = 0
for n in range(4, N + 1):
    str_n = str(n)
    if '1' not in str_n and '2' not in str_n and '3' not in str_n and '5' not in str_n and '6' \
        not in str_n and '8' not in str_n and '9' not in str_n and '0' not in str_n:
        if max_n < n <= N:
                max_n = n

print(max_n)

## 동료 코드
# N = int(input())
# for i in range(N, 0,-1):
#     result = 0

#     for j in str(i):
#         if j == '4' or j =='7':
#             result += 1
#     if result == len(str(i)):
#         print(i)
#         break

## 동료 코드 2
# n = int(input())

# for i in range(n):
#     num = n - i
#     error = 0

#     for j in str(num):
#         if j == "7" or j == "4":
#             pass
#         else:
#             error = 1
#             break
    
#     if error == 0:
#         break

# print(num)