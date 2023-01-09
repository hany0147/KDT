# 문자열을 입력받고
# 각 단어의 등장 횟수 출력

strings = input('문자열을 입력하세요 > ').split()

# print(type(strings)) # 리스트 타입

string_dict = {}

for string in strings:
    
    if string not in string_dict:
        string_dict[string]  = 1
    else:
        string_dict[string] += 1

for key, value in string_dict.items():
    print(key, value)