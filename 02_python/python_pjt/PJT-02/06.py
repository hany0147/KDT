import requests
from pprint import pprint


def credits(title):
    pass
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '0c59c5e11c98e00ab45095adaa0fbb6e',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title
    }
    res = requests.get(base_url+path, params=params).json()
    data = res['results']
    movie_id = 0

    if data == []:
        return None
    else:
        movie_id = data[0]['id']

    base_url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key' : '0c59c5e11c98e00ab45095adaa0fbb6e',
        'language' : 'ko-KR',
    }
    res = requests.get(base_url+path, params=params).json()
    data1 = res['cast']
    data2 = res['crew'] # data 리스트 유형
    # result = {}

    # for i in data1:
    #     if i['cast_id'] < 10:
    #         result['cast'] = i['name']
    # for i in data2:
    #     if i['department'] == 'Directing': 
    #         result['crew'] = i['name']
    
    # return result

    ## 이건 왜 안되지?




 ## 이런 방법도 있구나! (팀원것을 참조함 :))
    # return {
    #     'cast' : [i['name'] for i in data1 if i['cast_id'] < 10],
    #     'crew' : [a['name'] for a in data2 if a['department'] == 'Directing']
    # }



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
