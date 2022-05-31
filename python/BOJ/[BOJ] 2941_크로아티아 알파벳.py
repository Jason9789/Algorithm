croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = list(map(str, input()))
result = 0


while len(word) > 0:

    if ("".join(word[0:3])) in croatia:
        result += 1
        del word[0:3]

    elif ("".join(word[0:2])) in croatia:
        result += 1
        del word[0:2]

    else:
        result += 1
        del word[0]


print(result)
