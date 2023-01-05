n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
        # total = total + number * 2
        # 짝수면 해당 숫자에 2를 곱해서 total에 더하라

    elif number % 2 == 1:
        total += number + 1 * 3
        # total = total + number + 1 * 3
        # 홀수면 해당 숫자에 3을 더해서 total에 더하라


print(total) # 4 8 14 22 30 42 52 68 80 100

# 100