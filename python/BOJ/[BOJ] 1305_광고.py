
def failure(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(tmp)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j

    return tmp


L = int(input())
word = input()

table = failure(word)
print(table)

print(len(word) - table[len(word) - 1])
