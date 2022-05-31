
T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)

    result = ""

    for i in S:
        result += R * i

    print(result)
