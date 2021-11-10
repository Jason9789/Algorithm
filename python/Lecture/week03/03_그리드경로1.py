
m, n = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(m)]
dp = [[1]*n for _ in range(m)]

# for i in range(m):
#     for j in range(n):
#         print(grid[i][j], end=" ")
#     print()

# m, n까지 가는 서로 다른 경로의 개수 구하는 로직
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# for i in range(m):
#     for j in range(n):
#         print(dp[i][j], end=" ")
#     print()

print(dp[m-1][n-1] % 9999999)