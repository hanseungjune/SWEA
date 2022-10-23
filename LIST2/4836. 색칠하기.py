import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 필드 깔기
    field = [[0]*10 for _ in range(10)]
    # 색칠 횟수
    N = int(input())
    mx = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                field[r][c] += color
                if mx < field[r][c]:
                    mx = field[r][c]

    cnt = 0
    for row in field:
        for ele in row:
            if ele == mx:
                cnt += 1

    print(f'#{tc} {cnt}')



