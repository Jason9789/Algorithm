from collections import defaultdict


test = defaultdict(int)

print(test)

test[1] = 1

for i in range(2, 6):
    test[i] = test[i-1] + test[i-2]
    print(test)

print(test[4])
