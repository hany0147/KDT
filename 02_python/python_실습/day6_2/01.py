# 문자열을 입력받고, e가 처음 나오는 위치를 출력하세요.
# 만약 문자열에 e가 없으면 -1울 출력하세요.
# 예시: hello, hEllo hypergrowth, java


chr = -1
strings = input('문자열을 입력하세요 > ')
string_list = []

if 'e' not in strings:
    print(-1)
else:
    for string in strings:  # 요소 하나하나를 꺼내기 위해 for 문 사용
        string_list.append(string) # 요소를 모두 분리하기 위한 작업
        if string == 'e':
            break
    print(len(string_list) - 1)        

