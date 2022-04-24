# ===================================
# sudo-code

# DFS with recursion
# DFS(G, v)
#     label v as discovered
#     for all directed edges from v to w that are in G.adjacentEdges(v) do
#         if vertex w is not labeled as discovered then
#             recursively call DFS(G, w)

# 위의 수도 코드에는 정점 v의 모든 인접 유향(Directed) 간선들을 반복하라고 표기되어 있다.
# 위를 파이썬으로 구현하면 다음과 같다.

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)

    return discovered

# ===================================

# DFS with Stack
# DFS-iterative(G, V)
#     let S be a stack
#     S.push(V)
#     while S is not empty do
#         v = S.pop()
#         if v is not labeled as discovered then
#             label v as discovered
#             for all edges from v to w in G.adjacentEdges(v) do
#                 S.push(w)


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)

            for w in graph[v]:
                stack.append(w)

    return discovered
