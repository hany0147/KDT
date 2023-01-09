# 5를 입력 받으세요.

num = int(input())
print(number)

# 2 5 를 입력받아서 출력하세요.

a, b = list(map(int, input().split()))

print(a, b)


# 1 2 3을 입력받아서 출력하세요.

numbers = list(map(int, input().split()))
for number in numbers:
    print(number, end=" ")
    
# print(*numbers)
# *, 언패킹