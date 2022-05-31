N = int(input())

result = 0

for i in range(1, N+1):
    num_list = list(map(int, str(i)))

    if i < 100:
        result += 1

    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        result += 1


print(result)
