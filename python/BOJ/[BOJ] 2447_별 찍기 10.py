def draw(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3

    draw(a)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]


n = int(input())


Map = [[0 for i in range(n)] for i in range(n)]

draw(n)

for i in Map:
    for j in i:
        if j:
            print("*", end='')
        else:
            print(" ", end='')

    print()
