import sys
from collections import Counter


N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
counter = Counter(nums).most_common()

print(round(sum(nums)/N))
print(nums[N//2])
if len(counter) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])

else:
    print(counter[0][0])

print(nums[-1]-nums[0])
