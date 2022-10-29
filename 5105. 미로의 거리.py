import sys; sys.stdin=open('input.txt','r')
from collections import deque

def bfs(i, j):
    global visited, cnt
    queue = deque()
    queue.append((i, j, cnt))
    delta = [(1,0),(0,1),(0,-1),(-1,0)]
    while queue:
        y, x, cnt = queue.popleft()
        visited[y][x] = 1
        for d in range(4):
            ny = y + delta[d][0]
            nx = x + delta[d][1]
            cnt = cnt
            if 0<=ny<n and 0<=nx<n and (arr[ny][nx] == '0' or arr[ny][nx] == '2') and not visited[ny][nx]:
                if arr[ny][nx] == '2':
                    return cnt
                queue.append((ny, nx, cnt+1))
    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '3':
                ans = bfs(i, j)

    print(f'#{tc} {ans}')