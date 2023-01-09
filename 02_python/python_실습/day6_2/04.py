# 문자열과 알파벳을 공백으로 구분해서 입력받고
# 문자열에서 입력한 알파벳 개수 출력

strings = input('문자열을 입력하세요 > ').split()
cnt = 0
for string in strings[0]:
    if string == strings[1]:
        cnt += 1

print(cnt)