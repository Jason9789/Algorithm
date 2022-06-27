def solution(id_list, report, k):
    answer = []

    id_dict = {}
    banned_dict = {}

    for id in id_list:
        id_dict[id] = []
        banned_dict[id] = 0

    for i in range(len(report)):
        user, banned = report[i].split(" ")

        if banned not in id_dict[user]:
            id_dict[user].append(banned)

            banned_dict[banned] += 1

    for id in id_dict:
        cnt = 0

        for ban in id_dict[id]:
            if banned_dict[ban] >= k:
                cnt += 1

        answer.append(cnt)

    return answer
