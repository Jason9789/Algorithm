import re


def solution(new_id):
    answer = ''

    answer = new_id.lower()
    answer = re.sub('[^a-z0-9_.-]', '', answer)
    answer = re.sub('(([.])\\2{1,})', '.', answer)

    if answer and (answer[0] == '.'):
        answer = answer[1:]

    if answer and (answer[-1] == '.'):
        answer = answer[:len(answer)-1]

    if not answer:
        answer += "a"

    if len(answer) >= 16:
        answer = answer[:15]

        if answer and (answer[0] == '.'):
            answer = answer[1:]

        if answer and (answer[-1] == '.'):
            answer = answer[:len(answer)-1]

    if len(answer) <= 2:
        last = answer[-1]

        while len(answer) < 3:
            answer += last

    return answer
