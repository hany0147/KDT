import sys
sys.stdin = open('data/10950.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    num1, num2 = list(map(int, input().split()))
    print(num1 + num2)