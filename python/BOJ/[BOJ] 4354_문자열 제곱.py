# KMP 알고리즘

def failure(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j

    return tmp


while True:
    word = input()

    if word == '.':
        break

    table = failure(word)

    if len(word) % (len(table) - table[-1]) != 0:
        print(1)

    else:
        print(len(word) // (len(table) - table[-1]))
