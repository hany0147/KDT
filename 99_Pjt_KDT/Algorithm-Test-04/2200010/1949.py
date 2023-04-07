# 1949번 등산로 조성
'''
등산로를 만들기 위한 부지는 N * N 크기
최대한 긴 등산로를 만들 계획
각 숫자는 지형의 높이

등산로를 만드는 규칙은 다음과 같다.

① 등산로는 가장 높은 봉우리에서 시작해야 한다.
② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로
가로 또는 세로 방향으로 연결이 되어야 한다.
    즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

'''
# 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.


from pprint import pprint

N = 5
K = 1
mountain = [list(map(int, input().split())) for _ in range(5)]
# pprint(mountain)

start = max(mountain)

# 