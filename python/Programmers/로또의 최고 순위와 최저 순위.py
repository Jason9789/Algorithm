def solution(lottos, win_nums):
    answer = []

    lottos_set = set(lottos)
    win_nums_set = set(win_nums)

    min_rank = len(lottos_set & win_nums_set)
    zero_cnt = 0

    for i in sorted(lottos):
        if i == 0:
            zero_cnt += 1

    max_rank = min_rank + zero_cnt

    if max_rank == 6:
        answer.append(1)
    elif max_rank == 5:
        answer.append(2)
    elif max_rank == 4:
        answer.append(3)
    elif max_rank == 3:
        answer.append(4)
    elif max_rank == 2:
        answer.append(5)
    else:
        answer.append(6)

    if min_rank == 6:
        answer.append(1)
    elif min_rank == 5:
        answer.append(2)
    elif min_rank == 4:
        answer.append(3)
    elif min_rank == 3:
        answer.append(4)
    elif min_rank == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer
