import requests
from pprint import pprint


def recommendation(title):
    pass

    # id 찾기

    basic_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '0c59c5e11c98e00ab45095adaa0fbb6e',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title
    }
    
    movie_id = 0
    movies = requests.get(basic_url+path, params=params).json()
    data = movies['results']
    

    if data == []: # 추천 찾기 하기 전에 title이 없는 경우는 none값을 줘야 한다.
        return None
    else:
        movie_id = data[0]['id']

        # else 다음으로 추천영화 쭉~

    # 추천 영화

    basic_url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/recommendations'
    # 문자열 중 변수를 사용하려면 f스트링을 이용해야하는 걸 깜박하지말자!
    params = {
        'api_key' : '0c59c5e11c98e00ab45095adaa0fbb6e',
        'language' : 'ko-KR',
        'region' : 'KR'
    }
    movies = requests.get(basic_url+path, params=params).json()
    data  = movies['results']
    rec_list = []
    for rec in data:
        rec_list.append(rec['title'])

    return rec_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
