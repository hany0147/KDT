# if 5 >3:
#     print('크다!')
# else:
#     print('작다!')


# a = -10
# if a >= 0:
#     print('음수')
# else:
#     print('양수')
# print(a)

# num = int(input('0보다 큰 숫자를 입력하세요 > '))

# if num % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

dust = int(input())

if dust < 0 :
    print('0보다 큰 값을 입력하세요.')
else :
    if 30>= dust >= 0 :
        print('좋음')
    elif 80>= dust > 30 :
        print('보통')
    elif 150>= dust > 80 :
        print('나쁨')
    else :
        print('매우나쁨')
print('미세먼지 확인 완료!')
