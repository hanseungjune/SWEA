import sys;sys.stdin = open('input.txt','r')

# T = int(input())
# for tc in range(1, T+1):
#     size, cnt = map(int, input().split())
#     pizza = list(enumerate(list(map(int, input().split())), 1))
#     # print(pizza)
#     oven = []
#     for _ in range(size):
#         oven.append(pizza.pop(0))
#     # print(oven)
#
#     while len(oven) > 1:
#         if len(oven) < size and pizza:
#             oven.append(pizza.pop(0))
#         idx, cheese = oven.pop(0)
#         if not cheese//2:
#             continue
#         else:
#             oven.append((idx, cheese//2))
#
#     print(f'#{tc} {oven[0][0]}')

T = int(input())
for tc in range(1, T+1):
    size, cnt = map(int, input().split())
    pizza = list(enumerate(list(map(int, input().split())), 1))
    oven = []
    # print(pizza)
    for _ in range(size):
        oven.append(pizza.pop(0))
    # print(pizza)
    # print(oven)

    while len(oven) > 1:
        if len(oven) < size and pizza:
            oven.append(pizza.pop(0))
        idx, cheese = oven.pop(0)
        if cheese//2 == 0:
            continue
        else:
            oven.append((idx, cheese//2))

    print(f'#{tc} {oven[0][0]}')