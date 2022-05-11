T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    get_money = int(input())

    result = [0 for _ in range(8)]
    cnt = 0

    for i in money:

        cnt += get_money // i
        get_money -= (get_money // i) * i

        result[money.index(i)] = str(cnt)
        cnt = 0

    print(f"#{tc}\n{' '.join(result)}")
