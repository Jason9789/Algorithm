def check(list, length):
    cnt = 0

    for i in range(8):
        for j in range(9-length):
            word = list[i][j:j+length]
            if word == word[::-1]:
                cnt += 1

    return cnt


for tc in range(1, 11):
    length = int(input())

    grid = [[x for x in input()] for _ in range(8)]
    result = check(grid, length)

    new_grid = []

    # 90도 회전
    for i in range(8):
        tmp = []
        for j in range(8):
            tmp.append(grid[j][i])
        new_grid.append(tmp)

    result += check(new_grid, length)

    print(f'#{tc} {result}')
