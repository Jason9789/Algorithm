T = int(input())

for tc in range(1, T+1):
    N = int(input())

    distance = 0
    speed = 0

    for n in range(N):
        cmd = list(map(int, input().split()))

        if cmd[0] == 0:
            distance += speed
        elif cmd[0] == 1:
            speed += cmd[1]
            distance += speed

        elif cmd[0] == 2:
            if speed <= cmd[1]:
                speed = 0
            else:
                speed -= cmd[1]
            distance += speed

    print(f'#{tc} {distance}')
