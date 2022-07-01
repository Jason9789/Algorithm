def solution(N, stages):
    answer = {}

    size = len(stages)

    for stage in range(1, N+1):
        if size != 0:
            count = stages.count(stage)

            answer[stage] = count / size
            size -= count
        else:
            answer[stage] = 0

    return sorted(answer, key=lambda x: answer[x], reverse=True)
