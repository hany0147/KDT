# 1110번, 더하기 사이클

# 초기값 설정
N = input()
res = 0
cnt = 0
copy_N = int(N)

if int(N) == 0:
    print(1)
else:

# while 문: N과 res가 다를 때까지만 돌린다.
    while int(N) != int(res): ## 2번째 시행에서는 26 != 68

# copy_N값이 N과 동일한지 res와 동일한지 확인.

        if copy_N == int(N):
            copy_N = int(N)
        elif copy_N == int(res):
            copy_N = int(res)

        if copy_N >= 10: # 값이 10보다 클 때
            num = 0 # 결과 초기값
            n_list = [] # 리스트 초기값
            for n in str(copy_N): # 리스트에 넣을 문자들.
                n_list.append(n) # [문자, 문자]
            num = int(n_list[0]) + int(n_list[1]) # [숫자화 시켜 다시 더하기]
            res = n_list[1] + str(num)[-1] # 예시 68
            cnt += 1 # cnt = 1
            copy_N = int(res)
        elif copy_N < 10 and copy_N > 0: # res가 6일 때.
        # res = "0" + str(int(res)) # 06
            copy_N = "0" + str(copy_N)
            num = 0
            n_list = []
            for n in copy_N: # 리스트에 널 문자들.
                n_list.append(n) # 예시, 2 6
            num = int(n_list[0]) + int(n_list[1]) # 예시 8
            res = n_list[1] + str(num)[-1] # 예시 68
            cnt += 1 # cnt = 1
            copy_N = int(res)
        

    print(cnt)