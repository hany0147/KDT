# 공백으로 구분된 정수

import sys
sys.stdin = open("data/input1.txt", "r")


print((list(map(int, input().split()))))