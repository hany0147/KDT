# 2606번 바이러스
'''
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 
웜 바이러스에 걸리게 된다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''

N = int(input()) # 7(컴퓨터 수)
linked_coms = int(input()) # 6(직접 연결되어 있는 컴퓨터 쌍의 수)
graph = [[] for _ in range(N + 1)]

# 그래프 만들기
for _ in range(linked_coms):
    com1, com2 = list(map(int, input().split()))
    graph[com1].append(com2)
    graph[com2].append(com1)
print(graph)

# 체크리스트 만들기
visited = [False] * (N + 1)
# print(visited)

# 함수 만들기(DFS)
def dfs(start):
    stack = [start] # 돌아갈 곳 기록
    visited[start] = True # 시작 노드 방문 처리

    while stack: # 돌아갈 곳이 없을 때까지 반복
        cur = stack.pop() # 현재 방문 노드

        for adj in graph[cur]: # 인접한 모든 정점
            if not visited[adj]: # 아직 방문하지 않았다면
                visited[adj] = True # 방문 체크
                stack.append(adj) # 스택에 넣기
    return visited

cnt = 0

for i in dfs(1):
    if i == True:
        cnt += 1 


print(cnt - 1)

