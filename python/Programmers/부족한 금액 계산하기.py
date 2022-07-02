def solution(price, money, count):
    answer = price

    for i in range(2, count+1):
        answer += price * i

    if answer > money:
        answer -= money
    else:
        answer = 0
    return answer
