import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 

# movie는 dict, genres_list는 list 유형

this_movie_ids = movie['genre_ids']
result = []

for i in genres_list:
    if this_movie_ids[1] == i['id']:
        result.append(i['name'])
    if this_movie_ids[0] == i['id']:
        result.append(i['name'])

print(result)    

# genre_list = []
# for genre_id in this_movie_ids:
    # for genre_dict in genre_list:
        # if genre_id == genre_dict['id']:
            # genre_list.append(genre_dict['name'])