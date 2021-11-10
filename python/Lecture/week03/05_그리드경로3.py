
def solution(m, n, grid):

    dp = [ 0 for _ in range(n)]
    dp_pre = [ 0 for _ in range(n)]

    # 1차원 배열에 grid의 첫 번째 줄의 값을 저장 -> 이후 값들을 저장할 용도
    for i in range(n):
        dp[i] = grid[0][i]

    for i in range(1, m):
        # grid의 두번째 줄일 경우에는 첫 번째 줄에서 움직인 최소 비용 경로만 정하면 되기 때문에
        # i가 1인지, 그 이상인지를 나누었다.
        if i == 1:
            for j in range(n):
                # 만약에 grid에 주어진 n의 값이 1일 경우에는 단순히 이전의 값들만 더하면 된다.
                if n == 1:
                    dp[j] = grid[i][j] + grid[i-1][j]
                else:
                    # j == 0인 경우는 가장 왼쪽에 있는 경우다. 따라서 현재 위치에서 바로 위와 오른쪽 대각선을 확인하면 된다.
                    if j == 0:
                        dp[j] = grid[i][j] + min(grid[i-1][j], grid[i-1][j+1])

                    # j == n-1인 경우는 가장 오른쪽에 있는 경우다. 따라서 현재 위치에서 바로 위와 왼쪽 대각선을 확인하면 된다.
                    elif j == n-1:
                        dp[j] = grid[i][j] + min(grid[i-1][j], grid[i-1][j-1])

                    # 일반적인 경우이기에, 현재 위치에서 왼쪽 대각선, 바로 위, 오른쪽 대각선을 확인한다.
                    else:
                        dp[j] = grid[i][j] + min(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1])

            # 이 문제에서는 1차원 배열을 사용하여 부분 문제를 저장한다.
            # 따라서 루프가 끝날 때에 구한 부분 문제의 해들을 다음 루프에서 사용하기 위하여
            # dp_pre 라는 새로운 1차원 배열에 다시 저장해 넣는다.
            dp_pre = dp[:]

        # grid의 세번째 줄 이상일 때이다.
        # 두번째 줄은 이미 구해진 첫번째 줄의 값을 이용하여 부분 문제의 해를 구하면 됐는데,
        # 세번째 줄부터는 두번째 줄에 대한 부분 문제의 해. 즉 dp_pre의 값을 이용하여 부분 문제의 해룰 구한다.
        # 이때의 로직은 위와 같기에 생략한다.
        else:
            for j in range(n):
                if n == 1:
                    dp[j] = grid[i][j] + dp_pre[j]
                else:
                    if j == 0:
                        dp[j] = grid[i][j] + min(dp_pre[j], dp_pre[j+1])
                    elif j == n-1:
                        dp[j] = grid[i][j] + min(dp_pre[j], dp_pre[j-1])
                    else:
                        dp[j] = grid[i][j] + min(dp_pre[j-1], dp_pre[j], dp_pre[j+1])

            dp_pre = dp[:]


    # 1차원 배열 dp에는 각 경로의 최소 비용이 담겨져있다.
    # 전체 경로에서 최소 비용에 대한 경로를 구해야 하기 때문에, dp의 최솟값을 출력한다.
    return min(dp)



m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(solution(m, n, grid))