T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    result = 0

    if A == B:
        result = C
    elif A == C:
        result = B
    else:
        result = A

    print(f'#{tc} {result}')
