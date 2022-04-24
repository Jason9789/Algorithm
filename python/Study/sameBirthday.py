import random

TRIALS = 100000
same_birthdays = 0

# 10만 번 실험
for _ in range(TRIALS):
    birthdays = []

    # 23명이 모였을 때, 생일이 같을 경우 same_birthdays += 1
    # 23명이 모였을 땐 50.698%
    # 57명이 모였을 땐 99.087%의 확률로 생일이 같다.
    for i in range(57):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break

        birthdays.append(birthday)


# 전체 10만 번 실험 중 생일이 같은 실험의 확률
print(f'{same_birthdays / TRIALS * 100}%')
