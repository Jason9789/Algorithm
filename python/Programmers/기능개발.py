def solution(progresses, speeds):
    answer = []
    deploy = 0
    prog = progresses
    sp = speeds

    while progresses:
        p = progresses[0]

        if p < 100:
            for i, v in enumerate(prog):
                prog[i] += sp[i]

            if deploy > 0:
                answer.append(deploy)
                deploy = 0

        else:
            prog.pop(0)
            speeds.pop(0)
            deploy += 1

    if deploy > 0:
        answer.append(deploy)
        deploy = 0

    return answer
