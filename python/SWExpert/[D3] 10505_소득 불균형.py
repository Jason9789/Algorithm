T = int(input())

for tc in range(1, T+1):
    N = int(input())

    people = list(map(int, input().split()))

    average = sum(people) // N
    result = 0

    for p in people:
        if average >= p:
            result += 1

    print(f'#{tc} {result}')
