# 2720번 세탁소 사장 동혁

'''
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수,
다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수,
페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.

거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.

예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
'''

# dict 이용

# 입력

T = int(input())

for t in range(T):

    # 거스름 돈의 액수는 센트로 입력됨
    C = int(input())
    # print(C) # 1달러 = 100센트 124센트면 1.24달러

    remain_c= 0
    remain_dic = {} # dict 이용
    
    # 손님이 받는 동전의 개수를 최소로 하려면, 가장 많은 돈부터 나눠야 한다.
    remain_dic['Quarter'] = C // 25
    remain_c = C % 25

    remain_dic['Dime'] = remain_c // 10
    remain_c = remain_c % 10

    remain_dic['Nickel'] = remain_c // 5
    remain_c = remain_c % 5

    remain_dic['Penny'] = remain_c // 1
   
    lst = []
    for key, value in remain_dic.items():
       lst.append(value)

    print(*lst)    


# 동료 방식
# T = int(input())
# rest = [25,10,5,1]
# for i in range(T):
#     n = int(input())
#     for j in range(4):
#         print(n // rest[j],end=' ')
#         n = n % rest[j]
#     print()
# #####     