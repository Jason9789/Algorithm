T = int(input())

for tc in range(1, T+1):
    sudoku = [[int(x) for x in input().split()] for _ in range(9)]

    flag = 1

    # 행 검사
    for i in range(len(sudoku)):
        check = []
        for j in range(len(sudoku[0])):
            if sudoku[i][j] in check:
                flag = 0
                break
            else:
                check.append(sudoku[i][j])

    # 열 검사
    for i in range(len(sudoku)):
        check = []

        for j in range(len(sudoku[0])):
            if sudoku[j][i] in check:
                flag = 0
                break
            else:
                check.append(sudoku[j][i])

    # 3 x 3 검사
    for i in range(0, len(sudoku), 3):
        for j in range(0, len(sudoku), 3):
            check = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if sudoku[k][l] in check:
                        flag = 0
                        break
                    else:
                        check.append(sudoku[k][l])

    print(f'#{tc} {flag}')
