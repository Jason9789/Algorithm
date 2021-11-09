import sys

def stairs(n, cost):
    cost.insert(0, 0)
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = cost[1]
    dp[2] = cost[2]

    for i in range(3, n+1):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

    return dp[n]

n = int(input())
cost = list(map(int, sys.stdin.readline().split()))

print(stairs(n, cost))