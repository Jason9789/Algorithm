from pprint import pprint


def solution(survey, choices):
    answer = ''

    type = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }

    for i, s in enumerate(survey):

        agree = s[1:]
        disagree = s[:1]
        choice = choices[i]

        # 선택대로 성격 유형의 점수 넣기
        if choice == 1:
            type[disagree] += 3
        elif choice == 2:
            type[disagree] += 2
        elif choice == 3:
            type[disagree] += 1
        elif choice == 4:
            continue
        elif choice == 5:
            type[agree] += 1
        elif choice == 6:
            type[agree] += 2
        elif choice == 7:
            type[agree] += 3

    pprint(type)

    # RT Type
    if type["R"] < type["T"]:
        answer += "T"
    elif type["R"] > type["T"]:
        answer += "R"
    else:
        answer += "R"

    # CF Type
    if type["C"] < type["F"]:
        answer += "F"
    elif type["C"] > type["F"]:
        answer += "C"
    else:
        answer += "C"

    # JM Type
    if type["J"] < type["M"]:
        answer += "M"
    elif type["J"] > type["M"]:
        answer += "J"
    else:
        answer += "J"

    # AN Type
    if type["A"] < type["N"]:
        answer += "N"
    elif type["A"] > type["N"]:
        answer += "A"
    else:
        answer += "A"

    print(answer)
    return answer
