# num = int(input('1보다 큰 정수를 입력하세요. > '))
# a = 1
# n = 1
# while n <= num:
#     a = a + (1*n)
#     print(a)
#     n = n + 1
# print("끝")


# 변수는 항상 초기화
# 결과값을 담을 것도 준비해놓아라.
# 실행되는 순서도 너무나도 중요
# 종료 조건을 잘 설정해야 한다.

num = int(input('1보다 큰 정수를 입력하세요. > '))
n = 0
result = 0
while n <= num:
    result += n
    n += 1
    print(result, n)

print(result)

"""
0 1
1 2
3 3
6 4
10 5
15 6
...
"""


# for의 기본!
# 반복가능한 객체
# 통을 만들어놔야 한다. 
# 숫자통(range)

for i in range(1, num + 1):
    # result = result + n
    result += n

print(result)
