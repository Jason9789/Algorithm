T = int(input())

for i in range(T):
    nums = list(map(int, input().split()))
    s = 0
    results = []
    for j in nums:
        if j % 2 == 1:
            s += j
    print('#{0} {1}'.format(i+1, s))
