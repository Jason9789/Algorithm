T = int(input())

for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    time = 0

    if L <= X and X <= U:
        time = 0
    elif L > X:
        time = L - X
    else:
        time = -1

    print(f'#{tc} {time}')
