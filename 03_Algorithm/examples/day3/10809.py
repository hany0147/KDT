# 10809번 알파벳찾기
'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

# print(ord('z')) # 97  ~ 122

# strings = input()
# alp_list = []

# for i in range(97, 123):
#     alp = chr(i)
#     if alp in strings:
#         alp_list.append(strings.find(alp))
#     else:
#         alp_list.append(-1)


# print(*alp_list, sep = " ")


strings = input()
alp_list = []

for i in range(97, 123):
    alp = chr(i)
    alp_list.append(strings.find(alp))


print(*alp_list, sep = " ")
