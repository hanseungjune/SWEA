import sys; sys.stdin=open('../input.txt', 'r')

def dfs(st, graph, visited):
    global en, ans
    if st == en:
        ans = 1
        return

    else:
        for i in graph[st]:
            if not visited[i]:
                visited[i] = 1
                dfs(i, graph, visited)

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 출발, 도착
    st, en = map(int, input().split())

    ans = 0
    dfs(st, graph, visited)

    print(f'#{tc} {ans}')