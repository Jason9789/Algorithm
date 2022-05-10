T = int(input())

for tc in range(1, T+1):
    nums = [int(x) for x in input().split()]
    nums.sort()

    result = sum(nums[1:-1]) / len(nums[1:-1])
    print(nums[1:-1])

    print(f'#{tc} {round(result)}')
