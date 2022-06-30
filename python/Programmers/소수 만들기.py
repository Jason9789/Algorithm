from itertools import combinations
import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    check_prime = list(combinations(nums, 3))

    for c in check_prime:
        if is_prime_number(sum(c)):
            answer += 1

    return answer
