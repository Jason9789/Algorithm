T = int(input())

for T in range(1, T+1):
    N, M = map(int, input().split())
    flapper = []
    for i in range(N):
        flapper.append(list(map(int, input().split())))

    result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):

            fly_sum = 0

            for k in range(M):
                for l in range(M):
                    fly_sum += flapper[k+i][l+j]

            result = max(result, fly_sum)

    print(f'#{T} {result}')
