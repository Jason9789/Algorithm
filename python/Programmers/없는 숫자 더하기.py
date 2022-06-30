def solution(numbers):
    nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    answer = sum(nums - set(numbers))
    return answer
