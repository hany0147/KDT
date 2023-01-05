cnt_str = input('문자열을 입력하세요 > ')
cnt = 0

for i in cnt_str:
    if i == 'a':
        cnt += 1
    if i == 'A':
        cnt += 1
    if i == 'e':
        cnt += 1
    if i == 'E':
        cnt += 1
    if i == 'o':
        cnt += 1
    if i == 'O':
        cnt += 1
    if i == 'u':
        cnt += 1
    if i == 'U':
        cnt += 1

print(cnt)

# 더 단순하게 줄일 수 있는 방법이 없을까?