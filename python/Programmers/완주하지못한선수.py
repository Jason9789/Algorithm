from collections import Counter


def solution(participant, completion):
    # answer = ''

    # dict = {}

    # for p in participant:
    #     if p in dict:
    #         dict[p] += 1
    #     else:
    #         dict[p] = 1

    # for c in completion:
    #     if c in dict:
    #         dict[c] -= 1

    # for i in dict:
    #     if dict[i] > 0:
    #         answer = i

    # return answer

    answer = list(Counter(participant) - Counter(completion))

    return answer[0]
