import sys; sys.stdin=open('input.txt','r')

def dfs(i, j):
    global ans
    visited = [[0]*n for _ in range(n)]
    # 상하좌우
    delta = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    stack = [(i, j)]

    while stack:
        y, x = stack.pop()
        if arr[y][x] == 2:
            ans = 1
            return
        for i in range(4):
            ny = y + delta[i][0]
            nx = x + delta[i][1]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] != 1:
                visited[ny][nx] = 1
                stack.append((ny, nx))
    return

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = 0
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                dfs(i, j)

    print(f'#{tc} {ans}')