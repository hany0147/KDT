import sys
sys.stdin = open('data/10953.txt', 'r')

T = int(input())

for t in range(0, T):
    num1, num2 = list(map(int, input().split(',')))
    print(num1 + num2)