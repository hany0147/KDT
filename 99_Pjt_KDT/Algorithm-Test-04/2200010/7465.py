# 7465번 창용 마을 무리의 개수
'''
창용 마을에는 N명의 사람이 살고 있다.
사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.

두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.

창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.
'''

# 그래프 개념 (dfs)

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = [[] for _ in range(N + 1)]

    # 그래프
    for _ in range(M):
        x, y = list(map(int, input().split()))
        lst[x].append(y)
        lst[y].append(x)
    # print(lst)

    visited = [0 for _ in range(N + 1)]
    # print(visited)

    def dfs(start):
        stack = [start] # 기록
        visited[start] = 1
        
        
        while stack: # 빌때까지 기록
            cur = stack.pop() # 현 정점

            for adj in lst[cur]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = 1
        string = ''
        for i in visited:
            string += str(i)
        return string



    cnt_lst = []
    cnt = 0

    for n in range(1, N + 1):
        if dfs(n) not in cnt_lst:
            cnt_lst.append(dfs(n))
            cnt += 1

    print(f'#{t} {cnt}')
    

