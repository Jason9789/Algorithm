# 05/09 12:26 ~ 12:47

T = int(input())

for t in range(1, T+1):
    n = int(input())
    pascal = [[0] * n for _ in range(n)]

    print(f'#{t}')
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                pascal[i][j] = 1

            elif i > 1:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

            print(pascal[i][j], end=" ")
        print()
