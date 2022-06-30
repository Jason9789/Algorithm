from itertools import permutations


def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = list(set(nums))

    for _ in nums:
        if answer < length:
            answer += 1
    return answer
