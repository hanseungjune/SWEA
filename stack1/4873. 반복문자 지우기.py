import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    # lst.sort()
    # print(lst)

    stack = []
    for i in lst:
        if stack and stack[-1] == i:
            a = stack.pop()
        elif not stack or stack[-1] != i:
            stack.append(i)

    print(f'#{tc} {len(stack)}')