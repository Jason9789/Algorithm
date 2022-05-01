import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if target > nums[mid]:
#                 left = mid + 1

#             elif target < nums[mid]:
#                 right = mid - 1

#             else:
#                 return mid

#         return -1
