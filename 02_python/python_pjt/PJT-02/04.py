import requests
from pprint import pprint


def search_movie(title):
    pass
    
    basic_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '0c59c5e11c98e00ab45095adaa0fbb6e',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title
    }
    movies = requests.get(basic_url+path, params=params).json()
    data = movies['results']   # 영화 api 중 입력한 title 중 result 값 도출(타입:리스트)
    # pprint(data)
    # data를 출력했을 때, 검색할 수 없는 영화의 경우 [] '빈 리스트'를 출력한다.

    if data == []: # 고로 data값이 []이면 None을 반환하고
        return None
    else: # data값이 있으면, data의 첫번째 dict 중 키 'id'의 value를 반환하라.
        return data[0]['id']

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    pprint(search_movie('기생충'))
    # 496243
    pprint(search_movie('그래비티'))
    # 959101
    pprint(search_movie('검색할 수 없는 영화'))
    # None
