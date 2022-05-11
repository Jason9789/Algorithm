from cmath import inf


T = int(input())


def check(long, short):
    max_value = -999999
    for i in range(len(long) - len(short) + 1):
        arr_sum = 0

        for j in range(len(short)):
            arr_sum += long[i+j] * short[j]

        max_value = max(max_value, arr_sum)

    return max_value


for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N > M:
        result = check(arr1, arr2)
    else:
        result = check(arr2, arr1)

    print(f'#{tc} {result}')
