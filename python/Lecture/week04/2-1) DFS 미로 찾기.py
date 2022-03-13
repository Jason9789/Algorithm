import sys

class Position:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

# map : 미로 정보 저장하는 2차원 배열
# m, n : 미로의 행과 열 크기
# start, dest : 출발지와 목적지
# visited: 미로의 행과 열의 각 위치가 방문되었는지 판단하는 2차원 배열
def findPath(map, m, n, start, dest, visited):
    next = Position()

    # 시작점이 1 일 때
    if map[start.row][start.col] == 1:
        # 방문 했으면 True
        visited[start.row][start.col] = True
    else:
        return False

    if start.row == dest.row:
        return True

    # 오른쪽으로 이동
    if start.col < n-1:
        if map[start.row][start.col+1] == 1 and not visited[start.row][start.col+1]:
            next.row = start.row
            next.col = start.col + 1

            if findPath(map, m, n, next, dest, visited):
                return True

    # 아래로 이동
    if start.row < m - 1:
        if map[start.row + 1][start.col] == 1 and not visited[start.row + 1][start.col]:
            next.row = start.row + 1
            next.col = start.col
            if findPath(map, m, n, next, dest, visited):
                return True

    # 왼쪽으로 이동
    if start.col > 0:
        if map[start.row][start.col - 1] == 1 and not visited[start.row][start.col - 1]:
            next.row = start.row
            next.col = start.col - 1
            if findPath(map, m, n, next, dest, visited):
                return True

    # 위쪽으로 이동
    if start.row > 0:
        if map[start.row - 1][start.col] == 1 and not visited[start.row - 1][start.col]:
            next.row = start.row - 1
            next.col = start.col
            if findPath(map, m, n, next, dest, visited):
                return True

    # 모든 방향으로 이동할 수 없으면 False
    return False


m, n = map(int, input().split())
maze = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

for i in range(m):
    temp = input()
    maze[i] = list(map(int, list(str(temp))))

for i in range(n):
    answer = findPath(maze, m, n, Position(0, i), Position(m - 1, None), visited)
    if answer:
        break

if answer:
    print(1)
else:
    print(-1)


# 6 10
# 0110000011
# 1101111101
# 1101010111
# 1111010111
# 0100111000
# 1011110111