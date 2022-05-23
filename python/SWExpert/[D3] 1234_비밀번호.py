for tc in range(1, 11):
    N, nums = input().split()

    stack = []
    for n in nums:
        if not stack or (stack[-1] != n):
            stack.append(n)

        else:
            stack.pop()

    print(f"#{tc} {''.join(map(str, stack))}")
