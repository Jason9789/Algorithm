row, column = 5, 5
queries = [[2, 2, 4, 4]]    # x1, y1, x2, y2 (x1, y1 부터 x2, y2 범위)

arr = [[0] * column for _ in range(row)]
cnt = 0

for i in range(row):
    for j in range(column):
        cnt += 1
        arr[i][j] = cnt

for i in arr:
    print(*i, end='')
    print()

for t, l, b, r in queries:
    # index 계산을 편하게 하기 위해서 빼준다.
    top, left, bottom, right = t - 1, l - 1, b - 1, r - 1
    temp = arr[top][left]

    for k in range(top, bottom):    # 1번
        arr[k][left] = arr[k + 1][left]

    for k in range(left, right):    # 2번
        arr[bottom][k] = arr[bottom][k + 1]

    for k in range(bottom, top, -1):    # 3번
        arr[k][right] = arr[k - 1][right]

    for k in range(right, left, -1):    # 4번
        arr[top][k] = arr[top][k - 1]

    arr[top][left + 1] = temp    # temp 넣기

    for i in arr:
        print(*i, end=' ')
        print()
