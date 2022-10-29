import sys; sys.stdin=open('input.txt','r')

def backtrack(row, n, now_sum, visited):
    global min_sum
    if row == n:
        if now_sum < min_sum:
            min_sum = now_sum
            return

    elif now_sum > min_sum:
        return

    else:
        for col in range(n):
            if not visited[col]:
                visited[col] = 1
                backtrack(row+1, n, now_sum+arr[row][col], visited)
                visited[col] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 1e9
    visited = [0]*n
    backtrack(0, n, 0, visited)
    print(f'#{tc} {min_sum}')
