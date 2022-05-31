hour, minute = map(int, input().split())
time = int(input())

tmp_min = minute + time

result_min = tmp_min % 60
result_hour = (hour + (tmp_min // 60)) % 24


print(f'{result_hour} {result_min}')
