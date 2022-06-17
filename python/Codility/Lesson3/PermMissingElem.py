# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    n = len(A)
    result = 0

    check = [0 for _ in range(n+2)]

    for a in A:
        check[a] = 1

    # print(check)

    for i in range(1, len(check)):
        # print(i)
        if check[i] == 0:
            result = i

    return result
