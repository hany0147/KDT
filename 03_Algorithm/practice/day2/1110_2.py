# 1110번, 더하기 사이클(축약 버전 1)

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

        if copy_N < 10:
            copy_N = "0" + str(copy_N)
           
        num = 0 # 결과 초기값
        n_list = [] # 리스트 초기값
        for n in str(copy_N): # 리스트에 넣을 문자들.
            n_list.append(n) # [문자, 문자]
        num = int(n_list[0]) + int(n_list[1]) # [숫자화 시켜 다시 더하기]
        res = n_list[1] + str(num)[-1] # 예시 68
        cnt += 1 # cnt = 1
        copy_N = int(res)
        

    print(cnt)