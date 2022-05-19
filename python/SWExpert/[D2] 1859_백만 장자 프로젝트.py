T = int(input())

for tc in range(1, T+1):
    N = int(input())
    values = list(map(int, input().split()))

    max_value = 0
    max_profit = 0

    for v in range(N-1, -1, -1):
        print(values[v])
        if values[v] >= max_value:
            max_value = values[v]
        else:
            max_profit += (max_value - values[v])

    print(f'#{tc} {max_profit}')
