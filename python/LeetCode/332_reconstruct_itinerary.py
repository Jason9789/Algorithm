class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = collections.defaultdict(list)
        route = []

        # tickets을 그래프로 만들어 탐색하기 위함.
        # 또한, 사전 순서대로 정렬
        for a, b in sorted(tickets):
            graph[a].append(b)

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))

            route.append(a)

        dfs('JFK')

        return route[::-1]
