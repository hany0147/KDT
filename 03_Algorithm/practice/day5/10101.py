# 10101번 삼각형 외우기

'''
삼각형의 세 각을 입력받은 다음, 

세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.
'''
# 입력
A = int(input())
B = int(input())
C = int(input())


if (A + B + C) == 180: # 180 이라면
    # 각이 모두 같으면
    if A == B == C:
        print('Equilateral')
    # 두 각이 같은 경우
    elif (A == B) or (A == C) or (B == C):
        print('Isosceles')
    else:
        print('Scalene')

else: # 180이 아니면 삼각형이 아니다.
    print('Error') 
