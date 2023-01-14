import requests
from pprint import pprint


def ranking():
    pass
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=0c59c5e11c98e00ab45095adaa0fbb6e'
    res = requests.get(url).json()
    data = res.get('results') # 리스트 타입


    sort_data = sorted(data, key = lambda data : data['vote_average'], reverse = True)
      
    return sort_data[0:5]

'''
sorted함수(iterable, key=none, reverse=bool), reverse를 True로 놓으면, 내림차순 가능
key를 이용하면 커스텀 분류가 가능.
lambda 매개변수: 표현식
data의 dict 중 vote_average의 값을 sort의 분류기준으로 삼은 것
'''

# 아래의 코드는 수정하지 않습니다.

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
