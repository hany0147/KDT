import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

# 타입: list 

from pprint import pprint

new_list = []

for i in movies_list:
    new_info = {} # 어째서 for문 안에 넣어야하는가?

    new_info['id'] = i['id']
    new_info['title'] = i['title']
    new_info['poster_path'] = i['poster_path']
    new_info['vote_average'] = i['vote_average']
    new_info['overview'] = i['overview']
    new_info['genre_ids'] = i['genre_ids']
    new_list.append(new_info)
    
pprint(new_list)
