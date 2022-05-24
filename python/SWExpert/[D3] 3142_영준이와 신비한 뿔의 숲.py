T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    u = N - M
    t = M - u

    print(f'#{tc} {t} {u}')
