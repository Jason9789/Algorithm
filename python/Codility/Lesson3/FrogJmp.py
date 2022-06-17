# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    result = 0

    diff = Y - X

    if diff % D == 0:
        result = diff // D
    else:
        result = (diff // D) + 1

    return result
