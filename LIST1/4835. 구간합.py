import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # lst 갯수, 합의 범위
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # M-1 ~ N-M (범위)
    arr = []
    for i in range(M-1, N):
        a = sum(lst[i-M+1:i+1])
        arr.append(a)

    for j in range(0, N-M+1):
        b = sum(lst[j:j+M])
        if b not in arr:
            arr.append(b)

    mn = min(arr)
    mx = max(arr)
    ans = mx-mn
    print(f'#{tc} {ans}')


