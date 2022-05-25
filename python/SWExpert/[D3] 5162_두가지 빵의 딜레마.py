T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    select = min(A, B)

    result = C // select

    print(f'#{tc} {result}')
