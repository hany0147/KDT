# Max()함수 대신 쓰는 코드

number_list = [1, 2, 3, 4, 5]
result = 0

for i in number_list:
    if result >= i:
        result = result
    else:
        result = i
      
print(result)




number_list = [1, 1, 1]
result = 0

for i in number_list:
    if result >= i:
        result = result
    else:
        result = i
    
    
print(result)

# 나중에 이 문제는 다시 풀어보자.
# 좀 더 간략하게 할 방법이 있다.