import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    arr_rev = [list(x) for x in zip(*arr)]

    ans = ''
    for row in arr:
        for i in range(n-m+1):
            lst = row[i:m+i]
            lst_rev = lst[::-1]
            if lst == lst_rev:
                ans += ''.join(lst)

    for row in arr_rev:
        for i in range(n-m+1):
            lst = row[i:m+i]
            lst_rev = lst[::-1]
            if lst == lst_rev:
                ans += ''.join(lst)

    print(f'#{tc} {ans}')

