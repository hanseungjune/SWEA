import sys; sys.stdin=open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    lst = input().split()

    stack = []
    for i in lst:
        if i == '.':
            break

        if len(stack) >= 2 and i in '*/+-':
            b = stack.pop()
            b = int(b)
            a = stack.pop()
            a = int(a)
            if i == '+':
                ans = a + b
                stack.append(ans)
            elif i == '-':
                ans = a - b
                stack.append(ans)
            elif i == '*':
                ans = a * b
                stack.append(ans)
            elif i == '/':
                if b > a:
                    ans = b // a
                    stack.append(ans)
                else:
                    ans = a // b
                    stack.append(ans)
        elif len(stack) < 2 and i in '*/+-':
            ans = 'error'
            stack.append(ans)
            break
        else:
            stack.append(i)

    if len(stack) > 1:
        ans = 'error'
        stack.append(ans)

    print(f'#{tc} {stack[-1]}')