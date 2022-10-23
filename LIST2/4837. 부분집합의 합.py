import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    card = [i for i in range(1, 13)]

    cnt = 0
    lst = []
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(card[j])
        if temp not in lst and K == sum(temp) and N == len(temp):
            cnt += 1

    print(f'#{tc} {cnt}')