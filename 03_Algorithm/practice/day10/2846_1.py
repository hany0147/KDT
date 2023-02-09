# 오르막길 (강의)

# 첫 번째 숫자 : start, 마지막 숫자: end
# 값이 커지는 걸 확인 -> 값을 비교 -> 값이 커지는 지
# -> 나중에 나온 인덱스 값이 더 큰지 확인
# 비교의 주체를 나중 값으로 기준을 둠(i-1, i)

N = 5
list_ = [1,2,1,4,6]
max_lenth = 0
start = 0
end = 0

for i in range(1, N):

    # 오르막길 구간
    if list_[i] > list_[i-1]:
        # 시작을 해야 끝이 나올 수 있다.
        # start가 0일 때 해당 요소가 스타트가 될 수 있다.
        if start == 0:
            start = list_[i-1]
        

        # 마지막 인덱스도 오르막길일 때
        if i == N - 1:
            end = list_[i]
            length = end - start
        
            if max_length < length:
                max_length = length


    # 오르막길이 끝이날 때        
    elif list_[i] <= list_[i-1]:

        #오르막길이 시작했는지 확인
        if start != 0:
            end = list_[i-1]

        # 오르막길의 길이
            length = end - start
        
            if max_length < length:
                max_length = length

        # 새로운 오르막길의 시작을 위해서
        start = 0

