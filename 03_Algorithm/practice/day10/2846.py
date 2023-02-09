# 2846번 오르막길
'''
자전거 길은 오르막길, 내리막길, 평지로 이루어져 있다. 
상근이는 개강 첫 날 자전거를 타고 가면서 일정 거리마다 높이를 측정했다.
상근이는 가장 큰 오르막길의 크기를 구하려고 한다.

측정한 높이는 길이가 N인 수열로 나타낼 수 있다.
여기서 오르막길은 "적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열"이다. 
오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이이다.

예를 들어, 높이가 다음과 같은 길이 있다고 하자. 12 '3 5 7 10' 6 '1 11'.
이 길에는 2 개의 오르막길이 있다. 밑 줄로 표시된 부분 수열이 오르막길이다.

첫 번째 오르막길의 크기는 7이고, 두 번째 오르막길의 크기는 10이다.

높이가 12와 6인 곳은 오르막길에 속하지 않는다.

가장 큰 오르막길을 구하는 프로그램을 작성하시오.
'''

# 수가 계속 올라가면 쭉 가고, 아니면 멈춘다.

N = int(input())
heights = list(map(int, input().split()))
total_max = [] # 초기값
up_lst = [] # 초기값
max_height = 0

for height in heights:
    if len(heights) == 1:
        print(0)


    if height != heights[-1]:
    # height이 max_height 보다 클 경우 up_lst에 해당 height을 집어 넣는다.
        if max_height < height:
            up_lst.append(height)

        # 그리고 max_height에 해당 height값을 할당
            max_height = height
            print(f'#1: {up_lst}')
    # 만약 max_height이 height보다 크거나 같을 경우.
        elif max_height >= height:
            print(f'#2: {up_lst}')
        # 지금까지 진행한 up_list의 오르막길 크기를 구한다.
            total_max.append(up_lst[-1]- up_lst[0])
           
        
        # 그리고 up_lst와 max_height 비운뒤, 해당 height을 새로 추가한다.
            max_height = 0
            up_lst = []
            up_lst.append(height)
            print(f'#3: {up_lst}')

    else:
        if max_height < height:
            up_lst.append(height)
            print(f'#4: {up_lst}')
            total_max.append(up_lst[-1]- up_lst[0])
print(total_max)
print(max(total_max))

    



## 동료 코드


# n = int(input())
# n_list = list(map(int,input().split()))
# asc = []
# max_asc = 0
# for i in range(n-1):
#     asc.append(n_list[i+1] - n_list[i])
# for i in range(len(asc)):
#     sum = 0
#     if asc[i] >0:
#         sum+=asc[i]
#         for j in range(i+1,len(asc)):
#             if asc[j]>0:
#                 sum+=asc[j]
#             else:
#                 break
#         if max_asc < sum:
#             max_asc = sum
# print(max_asc)

# 요약하자면 asc 변수에 입력받은 값의 차이를 구해서 (+)면 더하고 (-)면 break되도록 구현해서 최댓값을 구했습니다!



####################################################################
# for height in heights:
#     if heights[-1] == height:
#         total_max.append(up_lst[-1] - up_lst[0])
#     else:
#         if max_height < height:
#             up_lst.append(height)
#             max_height = height
#             print(up_lst)
#         else:
#             total_max.append(up_lst[-1] - up_lst[0])
#             max_height = 0
#             up_lst = []
#             up_lst.append(height)

# print(total_max)
# print(max(total_max))


##########################################################

# for n in range(N):
#     # 인덱스 활용. 수열과 그 다음 수열의 값을 비교한다.
    
#     if n + 1 == N: # 익덱스 초과 방지
#         break

#     if heights[n] < heights[n + 1]: # 다음 수열이 크면 up_lst에 추가한다.
#         up_lst.append(heights[n])
#         up_lst.append(heights[n + 1])

#         if n + 2 == N:
#             total_max.append(up_lst[-1]- up_lst[0])

#     elif heights[n] >= heights[n + 1]: # 더 이상 수열이 커지지 않는다면     
#         if len(up_lst) >= 1:
#             total_max.append(up_lst[-1]- up_lst[0])
#         else:        # 만약 오르막길이 없는 경우에는 0을 출력한다.
#             up_lst = [0 for _ in range(N)]
#             total_max.append(up_lst[-1]- up_lst[0])

# print(total_max)       
# print(max(total_max))

   



