
def square(n, x):

    if x <= 1:
        return n
    else:
        return n * square(n, x-1)


for _ in range(10):
    T = int(input())

    num, exponent = map(int, input().split())

    result = square(num, exponent)

    print(f'#{T} {result}')
