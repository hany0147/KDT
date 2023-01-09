# with open('data/fruits.txt', 'r') as f:
#     cnt = 0
#     check = []
#     for line in f:
#         if 'berry' in line and 'berryfake' not in line:
#             if line not in check:
#                 cnt += 1
#                 check.append(line)
#     with open('data/03.txt', 'w') as i:
#         i.write(str(cnt))

        

fruits_cnt = 0
fruits_list = []

with open('data/fruits.txt', 'r') as f:
    fruits = f.readlines() # .readlines()는 파일의 모든 줄을 리스트로 읽어드는 것(=list(f))
    for fruit in fruits:
        fruit = fruit.strip() #.strip() 문자열에서 특정 문자 제거 / 매개변수가 제공되지 않으면 문자열의 시작과 끝의 공백 제거
        if fruit[-5:] == 'berry': # 뒤에 berry가 붙은 걸 찾아야 하니까, -5부터 끝까지
            if fruit not in fruits_list:
                fruits_list.append(fruit)
                fruits_cnt += 1

with open('data/03.txt', 'w') as f:
    f.write(str(fruits_cnt) + '\n') # 개행 \n해야 일렬로 나온다.
    for fruit in fruits_list:
        f.write(fruit + '\n')
