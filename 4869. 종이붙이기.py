import sys; sys.stdin=open('input.txt','r')

def f(n):
    if n <= 1:
        return 1

    else:
        return f(n-2)*2+f(n-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    ans = f(n)
    print(f'#{tc} {ans}')