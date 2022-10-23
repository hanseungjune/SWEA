import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # charge = 최대 이동거리, N = 마지막 정류장 번호, station = 충전소 수
    charge, N, station = map(int, input().split())
    number = list(map(int, input().split()))
    lst = [0]*(N+1)
    for n in number:
        lst[n] = 1
    flag = 0

    # 충전횟수
    cnt = 0
    i = N
    lst[-1] = -1
    while i > 0:
        i -= charge
        # print(lst)
        # print(i)
        # print(cnt)
        if i <= 0:
            break
        for _ in range(charge):
            # 충전소가 있다면,
            if lst[i] == 1:
                lst[i] = -1
                cnt += 1
                break
            # 충전소가 없다면,
            i += 1
        # 다 돌리고 또 이미 방문했다면?
        else:
            if lst[i] == -1:
                cnt = 0
                break

    print(f'#{tc} {cnt}')
