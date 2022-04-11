from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_maps = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_maps[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_maps and i != nums_maps[target - num]:
                return nums.index(num), nums_maps[target - num]
