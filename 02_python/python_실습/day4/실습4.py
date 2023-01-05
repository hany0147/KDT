dict_variable = {}

dict_variable['이름'] = input('이름을 입력하세요 > ')
dict_variable['전화번호'] = input('전화번호를 입력하세요 > ')
dict_variable['거주지'] = input('거주지를 입력하세요 > ')

print(dict_variable)

for key, value in dict_variable.items():
    print(f'{key} : {value}')

for key in dict_variable:
    print(f'{key} : {dict_variable[key]}')

    # for문에서 딕셔너리의 키값이 반환됨.
    # 따라서 값을 반환하고 싶으면, 변수[key] 해야 함. 