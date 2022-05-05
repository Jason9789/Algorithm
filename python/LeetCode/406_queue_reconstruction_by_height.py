class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []

        while heap:
            person = heapq.heappop(heap)

            # insert(a, b) : a번째 index에 b를 넣어라.
            result.insert(person[1], [-person[0], person[1]])

        return result
