
def dfs(graph, i, j):
    if i < 0 or i >= len(graph) or \
        j < 0 or j >= len(graph[0]) or \
            graph[i][j] != '1':
        return

    graph[i][j] = cnt

    # 동서남북 탐색
    dfs(graph, i + 1, j)
    dfs(graph, i - 1, j)
    dfs(graph, i, j + 1)
    dfs(graph, i, j - 1)


N = int(input())
graph = []
global cnt
cnt = 1

for _ in range(N):
    graph.append(list(map(str, input())))


# dfs
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '1':
            dfs(graph, i, j)

            cnt += 1

result = [0 for _ in range(cnt)]

# 배열 요소를 int로 바꾸기
for i in range(len(graph)):
    for j in range(len(graph[0])):
        graph[i][j] = int(graph[i][j])
        result[graph[i][j]] += 1

# for i in range(len(graph)):
#     print(graph[i])

# 정답
print(len(result)-1)

for i in result[1:]:
    print(i)

# n = int(input())
# graph = []
# num = []

# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def DFS(x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False

#     if graph[x][y] == 1:
#         global count
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             DFS(nx, ny)
#         return True
#     return False


# count = 0
# result = 0

# for i in range(n):
#     for j in range(n):
#         if DFS(i, j) == True:
#             num.append(count)
#             result += 1
#             count = 0

# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])
