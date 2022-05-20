
for tc in range(1, 11):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(N):
        r, c = 0, j
        stack = []

        while r < N:
            if not stack and grid[r][c] == 1:
                stack.append(grid[r][c])

            elif stack and grid[r][c] == 2:
                cnt += stack.pop()

            r += 1

    print(f'#{tc} {cnt}')
