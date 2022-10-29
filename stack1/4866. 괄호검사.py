import sys; sys.stdin=open('../input.txt', 'r')

def bracket_check(str):
    stack = []
    for i in str:
        if not stack and i in '({':
            stack.append(i)
        elif not stack and i in ')}':
            stack.append(i)

        elif stack and i in '({':
            stack.append(i)
        elif stack and i in ')}':
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)

    if stack:
        return 0
    elif not stack:
        return 1

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    ans = bracket_check(str1)
    print(f'#{tc} {ans}')

