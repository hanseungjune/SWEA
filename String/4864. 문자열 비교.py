import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    search = input()
    lst = input()

    sl = len(search)
    ll = len(lst)

    ans = 0
    for i in range(ll-sl+1):
        if lst[i:i+sl] == search:
            ans = 1

    print(f'#{tc} {ans}')