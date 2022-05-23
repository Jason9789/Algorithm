weeks = {
    "MON": 1,
    "TUE": 2,
    "WED": 3,
    "THU": 4,
    "FRI": 5,
    "SAT": 6,
    "SUN": 7
}

T = int(input())

for tc in range(1, T+1):
    day = input()

    result = 0

    if day == "SUN":
        result = 7
    else:
        result = 7 - weeks[day]

    print(f'#{tc} {result}')
