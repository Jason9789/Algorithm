d_list = [2, 3, 5, 7, 11]

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    result = []
    d = 2
    cnt = 0

    while N != 1 or d <= 11:
        if N % d == 0:
            N /= d
            cnt += 1

        else:
            if d in d_list:
                result.append(cnt)
                cnt = 0
            d += 1

    print(f'#{tc} {" ".join(map(str, result))}')
