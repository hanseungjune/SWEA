import sys;sys.stdin=open('input.txt','r')
from collections import deque

def bfs(st, en):
    global visited, graph, ans
    queue = deque()
    cnt = 0
    queue.append((st, cnt))
    visited[st] = 1

    while queue:
        x, cnt = queue.popleft()
        if x == en:
            ans = cnt
            return
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i, cnt+1))
    return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    ans = 0

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    st, en = map(int, input().split())
    bfs(st, en)

    print(f'#{tc} {ans}')