
def solution(m, n, grid, p, q):
    # 최소비용을 구하기 위한 dp 배열 초기화
    dp = [[0] * n for _ in range(m)]

    # i = 0, j = 0의 최소 비용 배열 값 초기화
    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]

    # (0, 0)부터 (p, q)까지의 최소 비용
    for i in range(1, p):
        for j in range(1, q):
            dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])


    for i in range(p-1, m):
        for j in range(q-1, n):
            if j == q-1 and i == p-1:
                continue
            elif j == q-1:
                dp[i][j] = grid[i][j] +dp[i-1][j]
            elif i == p-1:
                dp[i][j] = grid[i][j] + dp[i][j-1]


    for i in range(p, m):
        for j in range(q, n):
            if dp[i][j] == 0:
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

    return dp[m-1][n-1]


# 입력 부분
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
p, q = map(int, input().split())

print(solution(m, n, grid, p, q))
