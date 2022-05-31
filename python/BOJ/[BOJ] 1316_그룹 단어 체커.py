N = int(input())

result = 0

for _ in range(N):
    word = input()
    tmp = []
    flag = True

    for w in word:
        if w not in tmp:
            tmp.append(w)

        elif w in tmp and tmp[-1] == w:
            continue

        elif w in tmp:
            flag = False
            break

    if flag:
        result += 1


print(result)
