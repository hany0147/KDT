import requests


def popular_count():
    pass
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=0c59c5e11c98e00ab45095adaa0fbb6e'
    res = requests.get(url).json()
    data = res.get('results') # data = res['results'] # data의 타입: 리스트

    return len(data)
   
    # cnt = 0  # for 문 대신 'len' 가능
    # for i in data:
    #     cnt += 1

    # return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20


# 주소(돌다리)도 두들겨 보고 건너자 ^^

# if __name__ == '__main__':

# 'if name == 'main':처럼 name 변수의 값이 'main'인지 확인하는 코드는 
# 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다.
#  즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.