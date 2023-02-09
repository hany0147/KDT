# 오르막길 _ 다시 도전

N = int(input())
lst = list(map(int, input().split()))

# 초기값 설정
# 수열의 시작 부분과 끝 부분을 확인하기 위한 설정
start = 0 
end = 0

# 가장 높은 오르막길 크기 변수를 넣기 위함
max_height = 0
height = 0

# 
for i in range(1, N):
    
    # 오르막길인 경우
    if lst[i-1] < lst[i]:
        
        # 또한 아직 시작하지 않았어야,
        if start == 0:
            # start가 정해진다.
            start = lst[i-1]

        # 그런데 만약 i가 마지막 인덱스라면
        if i == N - 1:

            end = lst[i]
            height = end - start

            if max_height < height:
                max_height = height

    # 오르막길이 아닌경우
    elif lst[i-1] >= lst[i]:
        
        # start가 0이 아닌 경우
        if start != 0:
        
        # end가 정해진다
            end = lst[i-1]
            height = end - start
            start = 0

    # 가장 큰 오르막길 크기 구하기
            if max_height < height:
                max_height = height

print(max_height)
