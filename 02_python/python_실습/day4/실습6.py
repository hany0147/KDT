word = input('문자열을 입력하세요 > ')
dict_word = {}

for key in word:
    if key not in dict_word:
        dict_word[key] = 1
        # i가 딕셔너리 키 안에 없으면 value값 1을 추가한다.
    else:
        dict_word[key] += 1
        # i가 딕셔너리 키 안에 있으면 해당 value값에 1을 더한다.

for key in dict_word:
    print(key, dict_word[key])

# 나중에 다시 풀어봐야한다. 혼자힘으로 푼게 아니니까.