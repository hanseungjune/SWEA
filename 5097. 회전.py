import sys; sys.stdin=open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    num_cnt, move_cnt = map(int, input().split())
    queue = input().split()
    # print(queue)
    top = 0
    end = len(queue)-1

    i = 0
    while i <= move_cnt-1:
        if top < end:
            top += 1
        elif top == end:
            top = 0
        i += 1

    print(queue[top])