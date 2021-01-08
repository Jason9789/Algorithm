# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         pair = []
#         nums.sort()
#
#         for n in nums:
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []
#
#         return sum


# 파이썬 다운 방식.
# 정렬된 리스트에서 짝수번째만 더해서 출력함.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])