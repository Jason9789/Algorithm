from itertools import combinations


def solution(numbers):
    answer = []

    for a, b in list(combinations(numbers, 2)):
        answer.append(a + b)

    return sorted(list(set(answer)))
