T = int(input())

for tc in range(1, T+1):
    time1, time2 = map(int, input().split())

    result = time1 + time2

    if result >= 24:
        result -= 24

    print(f'#{tc} {result}')
