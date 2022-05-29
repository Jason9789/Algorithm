T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0

    sorted_nums = sorted((nums))

    while sorted_nums != nums:

        for even in range(N):
            if (even % 2 == 0) and (even <= N-2) and (nums[even] > nums[even+1]):
                nums[even], nums[even+1] = nums[even+1], nums[even]

        for odd in range(N):
            if (odd % 2 == 1) and (odd <= N - 2) and (nums[odd] > nums[odd+1]):
                nums[odd], nums[odd+1] = nums[odd+1], nums[odd]

        result += 1

    print(f'#{tc} {result}')
