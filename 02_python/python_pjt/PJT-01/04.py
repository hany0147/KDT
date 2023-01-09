dict_word = {}

with open('data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
# 공백 제거

        if fruit not in dict_word:
            dict_word[fruit] = 1
        else:
            dict_word[fruit] += 1

with open('data/04.txt', 'w') as i:
    for fruit, cnt in dict_word.items():
        i.write(f'{fruit} {cnt} \n')



## 팀원의 코딩
# count = 0
# name = {}
# with open('data/fruits.txt', 'r', encoding='utf-8') as f:
#     while True:
#         line = f.readline().strip()
#         if not line:
#             break
#         try: # 딕셔너리에 이미 키가 있어? 그럼 카운팅 1 더해
#             name[line] += 1
#         except: # 없으면 키 생성하고 1로 주자
#             name[line] = 1
    
#     with open('data/04.txt', 'w', encoding='utf-8') as a:
#         for i in name:
#             a.write(f"{i} {name[i]}\n")
        
    