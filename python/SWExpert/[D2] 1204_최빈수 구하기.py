from collections import Counter


T = int(input())

for tc in range(1, T+1):
    test = int(input())

    array = list(map(int, input().split()))

    counter = Counter(array).most_common(1)[0][0]

    print(f'#{test} {counter}')
