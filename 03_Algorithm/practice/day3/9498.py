# 9498번 시험성적
'''
시험 점수를 입력받아 90 ~ 100점은 A,
 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
  나머지 점수는 F를 출력하는 프로그램을 작성하시오
'''

score = int(input())

if score < 60:
    print('F')
elif score <= 69:
    print('D')
elif score <= 79:
    print('C')
elif score <= 89:
    print('B')
else:
    print('A')