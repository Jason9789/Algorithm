def solution(periods, payments, estimates):
    answer = [0, 0]

    for i in range(len(periods)):
        # 가입 기간 2년 미만인 고객은 VIP 불가
        if periods[i] + 1 < 24:
            continue

        # 현재 등급
        current_membership = ''

        # 2년 이상 5년 미만 VIP
        current_year_pay = sum(payments[i])
        if (24 <= periods[i] < 60) and current_year_pay >= 900_000:
            current_membership = 'VIP'

        # 5년 이상 VIP
        elif (periods[i] >= 60) and ((600_000 <= current_year_pay < 900_000) or (current_year_pay >= 900_000)):
            current_membership = 'VIP'

        # if current_membership == 'VIP':
        #     print(f'current: {i}')

        # 다음 달 등급
        next_membership = ''
        next_periods = periods[i] + 1
        next_year_pay = sum(payments[i][1:]) + estimates[i]

        # print(f'next: {next_membership} {next_periods} {next_year_pay}')
        # 2년 이상 5년 미만 VIP
        if (24 <= next_periods < 60) and (next_year_pay >= 900_000):
            next_membership = 'VIP'

        # 5년 이상 VIP
        elif (next_periods >= 60) and ((600_000 <= next_year_pay < 900_000) or (next_year_pay >= 900_000)):
            next_membership = 'VIP'

        # if next_membership == 'VIP':
        #     print(f'next: {i}')

        if current_membership == '' and next_membership == 'VIP':
            answer[0] += 1

        if current_membership == 'VIP' and next_membership == '':
            answer[1] += 1

    return answer
