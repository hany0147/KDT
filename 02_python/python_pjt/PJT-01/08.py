import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성

# movie는 dict, genres_list는 list
# 출력은 '필요한 정보'로만 구성된 딕셔너리

# genre_name = [], 해당 장르의 이름으로 구성된 리스트 생성

from pprint import pprint

this_movie_ids = movie['genre_ids']
genre_name = []
new_dict = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview']
}

for i in genres_list:
    if this_movie_ids[0] == i['id']:
        genre_name.append(i['name'])
    if this_movie_ids[1] == i['id']:
        genre_name.append(i['name'])
    
new_dict['genre_names'] = genre_name


pprint(new_dict)