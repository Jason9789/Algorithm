from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        result = 0
        nums.sort()

        for i in range(len(nums)-1):
            if i % 2 == 0:
                # result.append(nums[i])
                result += nums[i]

        return result
