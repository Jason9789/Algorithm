T = int(input())

for tc in range(1, T+1):
    grade = list(map(int, input().split()))

    for i in range(len(grade)):
        if grade[i] < 40:
            grade[i] = 40

    average = sum(grade) // len(grade)

    print(f'#{tc} {average}')
