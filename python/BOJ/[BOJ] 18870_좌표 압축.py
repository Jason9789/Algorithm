import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums2 = sorted(list(set(nums)))
dict = {nums2[i]: i for i in range(len(nums2))}

for i in nums:
    print(dict[i], end=" ")
