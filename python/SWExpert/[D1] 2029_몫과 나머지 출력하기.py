T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())

    div, mod = a // b, a % b

    print('#{0} {1} {2}'.format(i, div, mod))
