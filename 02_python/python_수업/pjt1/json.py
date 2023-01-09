f = open('movie.json', 'r', encoding= 'UTF8')

print(f.read())


with open('movie.json', 'r', encoding= 'UTF8') as f:
    print(f.read())


## 정답
## 해당 파일의 경로를 파악하라!
# movie의 타입은 'dict'

import json
from pprint import pprint

with open('data/movie.json', 'r', encoding= 'UTF8') as f:
    movie = json.load(f)
    print(movie)





