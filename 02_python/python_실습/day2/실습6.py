# string = input('문자열을 입력하세요 > ')
# rev_string = string[: : -1]
# for char in rev_string:

#     print(char)


string = input('문자열을 입력하세요 > ')
for char in string[: : -1]:
    print(char)