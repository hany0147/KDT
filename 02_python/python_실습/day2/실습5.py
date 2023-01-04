num = int(input('정수를 입력하세요 > '))

if num > 100:
    print('에러')
elif num > 60:
    print('합격')
elif num < 0:
    print('에러')
else:
    print('불합격')