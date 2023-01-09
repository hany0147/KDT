# 문자열을 입력받고,
# e를 제거한 결과 출력

strings = input('문자열을 입력하세요 > ')
strings_list = []
# e가 있으면 e를 삭제하라(for문, if문)

for string in strings:
   if 'e' not in string:
      strings_list.append(string)

for i in strings_list:
   print(i, end = " ".strip())
       
