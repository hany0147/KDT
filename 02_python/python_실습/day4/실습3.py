dict_variable = {
    '이름': '정우영',
    '생년': '2000',
    '회사': '하이퍼그로스',
}

# 나이: 이번년도 - 생년 + 1
# 이번년월일: datetime.date.today()

import datetime

this_year = datetime.date.today()

# print(this_year.year)

# print(int(dict_variable['생년']))

# print(this_year.year - int(dict_variable['생년']) + 1)

print(f"나이 : {this_year.year - int(dict_variable['생년']) + 1}세")