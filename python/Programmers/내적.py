def solution(a, b):
    answer = 0

    for v1, v2 in zip(a, b):
        answer += (v1 * v2)

    return answer
