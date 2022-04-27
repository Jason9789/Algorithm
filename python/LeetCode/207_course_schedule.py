class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # Cycle을 만들면 False
            if i in traced:
                return False

            # 이미 방문한 노드이면 True
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제 및 방문 노드 추가
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
