n = int(input())
nums = []

nums = list(map(int, input().split()))

stack = []
result = [-1] * len(nums)

for i in range(len(nums)):

    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]

    stack.append(i)

print(*result)
