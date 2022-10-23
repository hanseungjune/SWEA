import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    for _ in range(5):
        mx = max(lst)
        mn = min(lst)
        print(mx, end=' ')
        print(mn, end=' ')
        lst.remove(mx)
        lst.remove(mn)
    print()

