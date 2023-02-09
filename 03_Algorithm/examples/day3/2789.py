# 2789번 유학금지
'''
 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다.
  즉, 어떤 이메일에 LOVA란 단어가 있다면, 
  A는 CAMBRIDGE에 포함된 알파벳이기 때문에, 받아보는 사람은 LOV로 받는다.

이렇게, 어떤 단어가 주어졌을 때, 
검열을 거친 후에는 어떤 단어가 되는지 구하는 프로그램을 작성하시오.
'''

words = input()
check = 'CAMBRIDGE'

for word in words:
  if word in check:
    new_word = words.replace(word, "")
    words = new_word

print(words) 

# 포함하지 않은 문자 출력하는 방법으로 코드 짜보자.