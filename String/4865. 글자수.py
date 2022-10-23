import sys; sys.stdin=open('../input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    str_dict = dict()

    for str in str1:
        if str not in str_dict:
            str_dict[str] = 0

    for key in str_dict.keys():
        for str in str2:
            if key == str:
                str_dict[key] += 1
    mx = 0
    for key, value in str_dict.items():
        if mx < value:
            mx = value

    print(f'#{tc} {mx}')
