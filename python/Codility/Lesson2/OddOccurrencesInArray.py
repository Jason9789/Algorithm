# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter


def solution(A):

    c = Counter(A)

    result = 0
    for key in c:
        if c[key] % 2 != 0:
            result = key

    return result
