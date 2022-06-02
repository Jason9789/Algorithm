from collections import deque


graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


# deque을 활용한 DFS
def dfs(graph, start_node):
    visited = []
    stack = deque()

    # 시작 노드 설정
    stack.append(start_node)

    # 방문이 필요한 리스트가 아직 존재한다면?
    while stack:

        # 시작 노드 지정
        node = stack.pop()

        # 만약 방문한 리스트에 없다면?
        if node not in visited:

            # 방문 리스트에 노드 추가
            visited.append(node)
            # 인접 노드들을 방문 예정 리스트에 추가
            stack.extend(graph[node])

    return visited


print(dfs(graph, 'A'))


# 재귀함수를 통한 DFS 구현
def dfs_recursive(graph, start, visited=[]):
    # 데이터를 추가
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited


print(dfs_recursive(graph, 'A'))
