num = int(input('정수를 입력하세요 > '))

if num >= 1:
    for i in range(num):
        if i % 2 == 0:
            continue
        print(i)
else:
    print(False)