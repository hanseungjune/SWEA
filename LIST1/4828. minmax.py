import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = abs(min(lst)-max(lst))
    print(f'#{tc} {ans}')
