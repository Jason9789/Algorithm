# ===================================
# sudo-code

# BFS(G, start_v)
#   let Q be a queue
#    label start_v as discovered
#     Q.enqueue(start_v)
#     while Q is not empty do
#         v := Q.dequeue()
#         if v is the goal then
#             return v
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as discovered then
#                 label w as discovered
#                 w.parent := v
#                 Q.enqueue(w)

def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered
