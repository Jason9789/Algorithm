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


def bfs(graph, start):
    stack, visited = [], []
    stack.append(start)

    while stack:
        node = stack[0]
        del stack[0]

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


print(bfs(graph, 'A'))
