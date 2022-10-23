import sys;sys.stdin = open('../input.txt', 'r')

def binary_search(target):
    global total
    left = 1
    right = total
    cnt = 0
    while left <= right:
        mid = int((left + right)/2)
        # 찾으면 출력
        if mid == target:
            return cnt
        elif mid < target:
            cnt += 1
            left = mid
        elif mid > target:
            cnt += 1
            right = mid

T = int(input())
for tc in range(1, T+1):
    # 전체쪽수, A에서 찾아야하는 쪽수, B에서 찾아야하는 쪽수
    total, tarA, tarB = map(int, input().split())
    cntA, cntB = 0, 0
    cntA = binary_search(tarA)
    cntB = binary_search(tarB)

    if cntA == cntB:
        print(f'#{tc} 0')
    elif cntA > cntB:
        print(f'#{tc} B')
    elif cntA < cntB:
        print(f'#{tc} A')
