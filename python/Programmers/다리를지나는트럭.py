def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing_truck = [0] * bridge_length

    while crossing_truck:
        answer += 1
        crossing_truck.pop(0)

        if truck_weights:
            if sum(crossing_truck) + truck_weights[0] <= weight:
                crossing_truck.append(truck_weights.pop(0))

            else:
                crossing_truck.append(0)

    return answer
