
numbers = list(range(1, 10_001))
remove_list = []

for i in range(1, 10001):
    tmp = i + sum(list(map(int, str(i))))

    if tmp <= 10000:
        remove_list.append(tmp)


for num in set(remove_list):
    numbers.remove(num)


for i in numbers:
    print(i)
