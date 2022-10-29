import sys; sys.stdin=open('input.txt','r')

def divide(left, right):
    if left == right:
        return left

    else:
        a = divide(left, (left+right)//2)
        b = divide((left+right)//2+1, right)
        return rsp(a, b)

def rsp(x, y):
    if cards[x] == cards[y]:
        return x
    elif cards[x] - cards[y] == 1 or cards[x] - cards[y] == -2:
        return x
    return y

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc} {divide(0, n-1)+1}')
