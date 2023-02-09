import sys
sys.stdin = open('data/10886.txt', 'r')

N = int(input())
agree = 0
not_agree = 0
for i in range(0, N):
    suv = int(input())
    if suv == 1:
        agree += 1
    elif suv == 0:
        not_agree += 1

if agree > not_agree:
    print('Junhee is cute!')
elif agree < not_agree:
    print('Junhee is not cute!')
