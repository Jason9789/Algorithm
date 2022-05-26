T = int(input())

for tc in range(1, T+1):
    N = int(input())
    avg = 0

    for _ in range(N):
        tmp = input().split()
        p = float(tmp[0])
        x = int(tmp[1])
        avg += p * x

    print(f'#{tc} {avg:.6f}')
