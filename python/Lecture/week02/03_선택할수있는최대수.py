def count(n, k):
    C = [[0 for j in range(n+1)] for i in range(n+1)] for i in range(n+1):
    for j in range(n+1): if j == 1:
        C[i][j] = 1 elif i == 0:
        C[i][j] = 1 elif i < j:
        C[i][j] = C[i][i] else:
        C[i][j] = C[i-j][j]+C[i][j-1]

    return C[n][n]