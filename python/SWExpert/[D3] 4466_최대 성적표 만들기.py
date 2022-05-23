T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    result = 0

    for i in range(K):
        result += arr[i]

    print(f'#{tc} {result}')
