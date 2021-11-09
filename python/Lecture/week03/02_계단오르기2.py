import sys

def stairs(n, s, cost):
    cost.insert(0, 0)

    dp = [0 for i in range(n+1)]

    # dp[0] = 0
    # s개의 계단을 오르는 가중치
    for i in range(1, s+1):
        dp[i] = cost[i]

    for i in range(s+1, n+1):
        tempList = []

        for j in range(1, s + 1):
            tempList.append(dp[i - j])
            # print(tempList)

        dp[i] = min(tempList) + cost[i]

    return dp[n]

n, s = map(int, input().split())
cost = list(map(int, sys.stdin.readline().split()))

print(stairs(n, s, cost))