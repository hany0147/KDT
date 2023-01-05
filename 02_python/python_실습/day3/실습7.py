# Min()함수 대신 쓰는 코드

number_list = [1, 2, 3, 4, 5]
min_value = number_list[0] 

# 초기값을 number_list에서 받아야 하니까!
# 리스트 활용력을 기르자.

for n in number_list:
    if n < min_value:
        min_value = n

print(min_value)



number_list = [5, 2, 5, 5]
min_value = number_list[0] 


for n in number_list:
    if n < min_value:
        min_value = n

print(min_value)
