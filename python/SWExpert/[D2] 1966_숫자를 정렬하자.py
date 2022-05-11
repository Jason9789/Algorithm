T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [0 for _ in range(N)]
    nums = list(map(int, input().split()))

    nums.sort()
    print(f"#{tc} {' '.join(map(str, nums))}")
