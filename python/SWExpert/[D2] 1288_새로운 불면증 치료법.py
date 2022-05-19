T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = [0] * 10
    i = 1

    while 0 in numbers:
        num = str(N * i)

        for n in range(len(num)):
            numbers[int(num[n])] += 1

        i += 1

    print(f'#{tc} {num}')
