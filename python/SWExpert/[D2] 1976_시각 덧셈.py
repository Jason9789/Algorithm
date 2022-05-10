T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    carry = 0
    m = 0

    if m1 + m2 >= 60:
        m = m1 + m2 - 60
        carry = 1
    else:
        m = m1 + m2

    h = 0

    if h1 + h2 + carry > 12:
        h = h1 + h2 + carry - 12
    else:
        h = h1 + h2 + carry

    print(f'#{tc} {h} {m}')
