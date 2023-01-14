# 1. 정수를 출력하세요
## 5

number = int(input())

print(number)


# 2. 단어를 구분해서 출력하세요
## hello python world

string = input().split()

print(string)

# 3. 테스트 케이스마다 입력 값을 그대로 출력하세요.
## 3테스트 케이스 수: 3, 입력코드(pass)?

test = int(input())

for i in range(1, test + 1):
    int(input())


# 4. 2개 이상의 정수를 출력하세요.
## 2 0 3 92 3

nums = list(map(int, input().split()))

print(*nums)


# 5. 2개의 정수를 출력하세요.
## 2 3

a, b = list(map(int, input().split()))
print(a, b)


# 6. 단어를 구분해서 출력하세요.
## I am Programmer

strings = input().split()
print(strings)

