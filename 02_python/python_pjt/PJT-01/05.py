import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성

## dict 타입 / 'genre_ids'는 리스트가 값

from pprint import pprint

new_movie_dic = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_ids': movie['genre_ids'],
}

pprint(new_movie_dic)

## 다른 방법
# new_movie_dic['id'] = movie['id']
# new_movie_dic['title'] = movie['title']
# new_movie_dic['vote_average'] = movie['vote_average']
# new_movie_dic['overview'] = movie['overview']
# new_movie_dic['genre_ids'] = movie['genre_ids']