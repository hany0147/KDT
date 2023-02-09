# 1110번, 더하기 사이클(축약 버전 2)

# 초기값 설정
N = int(input())
res = 100 # 제약 범위를 넘어선 값을 넣어서 절대 N값과 겹치지 않게 만들기(0<=N<=99)
cnt = 0
copy_N = N # N과 res를 자유롭게 할당하기 위하여 만든 변수

# while 문: N과 res가 다를 때까지만 돌린다.
while N != int(res): #예시: 26 ## 2번째 시행에서는 26 != 68

    if copy_N < 10:
        copy_N = "0" + str(copy_N) # 예시 5이면, 0 + 5 -> 05
           
    num = 0 # 더하기 변수 초기값
    n_list = [] # 리스트 초기값
    for n in str(copy_N): # 리스트에 넣을 문자들.
        n_list.append(n) # [문자, 문자] # 예시 2 6
    num = int(n_list[0]) + int(n_list[1]) # [숫자화 시켜 다시 더하기] # 예시 8
    res = n_list[1] + str(num)[-1] # 예시 68
    cnt += 1 # cnt = 1
    copy_N = int(res) # 첫 번째 시행 이후는 무조건 res값
        
print(cnt)