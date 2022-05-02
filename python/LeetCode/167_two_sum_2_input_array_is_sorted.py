class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []

        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp < target:
                left += 1

            elif tmp > target:
                right -= 1

            else:
                result.append(left + 1)
                result.append(right + 1)

                return result

        return -1
