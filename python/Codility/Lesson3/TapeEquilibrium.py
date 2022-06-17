# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    sum_left = 0
    sum_right = sum(A)

    result = float('inf')

    for i in range(1, len(A)):

        sum_left += A[i-1]
        sum_right -= A[i-1]
        diff = abs(sum_left - sum_right)

        result = min(result, diff)

    return result
