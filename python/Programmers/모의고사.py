
def solution(answers):
    answer = []
    check1 = [1, 2, 3, 4, 5] * (round(len(answers)//5) + 1)
    check2 = [2, 1, 2, 3, 2, 4, 2, 5] * (round(len(answers)//8) + 1)
    check3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (round(len(answers)//10) + 1)

    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == check1[i]:
            cnt1 += 1
        if answers[i] == check2[i]:
            cnt2 += 1
        if answers[i] == check3[i]:
            cnt3 += 1

    max_value = max(cnt1, cnt2, cnt3)

    if max_value == cnt1:
        answer.append(1)
    if max_value == cnt2:
        answer.append(2)
    if max_value == cnt3:
        answer.append(3)

    return answer
