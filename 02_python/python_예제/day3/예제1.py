list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()

 # .pop()일 경우, 디폴트로 마지막 숫자를 제거한다.

list_variable.append(7)
list_variable.append(8)

# .append()는 안에 무조건 변수를 넣어야 한다.

for element in list_variable[2:]:
    print(element, end = " ")

"""
2 3 4 5 7 8
"""