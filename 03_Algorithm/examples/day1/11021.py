import sys
sys.stdin = open('data/11021.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    num1, num2 = list(map(int, input().split()))
    print(f'Case #{t}: {num1 + num2}')
