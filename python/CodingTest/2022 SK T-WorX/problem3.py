def solution(n, plans, clients):
    answer = []

    m = len(plans)  # m개의 휴대폰 요금제
    arr_plans = []
    arr_clients = []

    # [입력] 입력받은 plans와 clients 배열로 만들기
    arr_plans.append(list(map(int, plans[0].split())))
    for i in range(1, len(plans)):
        arr_plans.append(list(map(int, plans[i].split())))
        arr_plans[i].extend(arr_plans[i-1][1:])  # 기존 부가 서비스 추가

    for i in range(len(clients)):
        arr_clients.append(list(map(int, clients[i].split())))

    # [구현]
    for i in arr_clients:
        check_plan = []             # 현재 가능한 플랜 체크하기
        check_service = []          # 사용자가 원하는 서비스가 플랜에 있는지 확인하기
        tmp_result = 0

        for j in range(len(arr_plans)):
            # 사용자가 원하는 서비스가 플랜에 있는지 확인하기
            check_service = set(i[1:]) - set(arr_plans[j][1:])
            # 사용자가 사용하는 요금제보다 플랜의 요금제가 높고, 사용자가 원하는 서비스가 다 존재할 때
            if i[0] <= arr_plans[j][0] and len(check_service) == 0:
                # 사용할 수 있는 플랜 저장하기
                check_plan.append(arr_plans[j])

                # 최소 사용 가능한 플랜을 찾으면 다음 사람을 체크 (효율)
                if len(check_plan) == 1:
                    tmp_result = j + 1
                    break

        answer.append(tmp_result)

    return answer
