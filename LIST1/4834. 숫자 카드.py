import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(input())
    lst.sort()

    # card
    card = dict()
    for num in lst:
        if num in card:
            card[num] += 1
        else:
            card[num] = 1

    mx = 0
    mx_key = 0
    for key, value in card.items():
        if mx <= value:
            mx = value
            mx_key = key

    print(f'#{tc} {mx_key} {mx}')






