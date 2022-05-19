T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    min_fee = 0

    if W <= R:
        min_fee = Q

    else:
        min_fee = Q + (W - R) * S

    min_fee = min(min_fee, P * W)

    print(f'#{tc} {min_fee}')
