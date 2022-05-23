T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    set_submit = set(submit)

    total = [x for x in range(1, N+1)]

    set_total = set(total)

    result = list(map(str, set_total - set_submit))

    print(f"#{tc} {' '.join(result)}")
