import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #         results = []
        #         prev_element = []

        #         def dfs(elements):

        #             if len(elements) == 0:
        #                 results.append(prev_element[:])

        #             # 순열 재귀
        #             for e in elements:
        #                 next_element = elements[:]
        #                 next_element.remove(e)

        #                 prev_element.append(e)
        #                 dfs(next_element)
        #                 prev_element.pop()

        #         dfs(nums)

        #         return results

        return list(itertools.permutations(nums))
