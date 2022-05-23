T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = 0

    if A >= 10 or B >= 10:
        result = -1

    else:
        result = A * B

    print(f'#{tc} {result}')
