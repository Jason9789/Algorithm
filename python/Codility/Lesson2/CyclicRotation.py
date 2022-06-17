# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(A, K):

    if not A:
        return []

    d = deque(A)

    for _ in range(K):
        d.appendleft(d.pop())

    return list(d)
