# 4406번 모음이 보이지 않는 사람.

T = int(input())
for t in range(1, T + 1):
    words = input()

    if 'a' in words:
        words = words.replace('a', '')
    if 'e' in words:
        words = words.replace('e', '')
    if 'i' in words:
        words = words.replace('i', '')
    if 'o' in words:
        words= words.replace('o', '')
    if 'u' in words:
        words = words.replace('u', '')

    print(f'#{t} {words}')
