# 4963번 섬의 개수
'''
정사각형으로 이루어져 있는 섬과 바다 지도
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은
걸어갈 수 있는 사각형
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

'''

# 입력
'''
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
너비 : w, 높이: h
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
땅: 1, 바다: 0
입력의 마지막 줄에는 0이 두 개 주어진다.
'''

w, h = list(map(int, input().split()))
temp = []

# 그래프 만들기.
for _ in range(w):
    map_ = list(map(int, input().split()))
    temp.append(map_)
# print(graph)

# 체크리스트 만들기
visited = [[False] * w for _ in range(h)]
# print(visited)

graph = []
for i in range(w):
    temp_graph = []
    for j in range(h):
        if temp[i][j] == 1:
            temp_graph.append((i, j))
        else:
            graph.append(temp_graph)
            temp_graph = []
            

    












# def dfs(start1, start2):
#     stack = [(start1, start2)]
#     visited[start1][start2] = True

#     while stack:
#         cur = stack.pop()

#         for adj1, adj2 in graph(cur):
#             if not visited:
#                 visited[adj1][adj2] = True
#                 stack.append((adj1, adj2))
#     return visited

# print(dfs(0,0))        

