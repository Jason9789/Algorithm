for tc in range(1, 11):
    N = int(input())

    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        max_height = 0

        if buildings[i] > buildings[i-2] and buildings[i] > buildings[i-1] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            max_height = max(
                buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])

            result += buildings[i] - max_height

    print(f'#{tc} {result}')
