
word = input()
result = 0

for w in word:
    if w in "ABC":
        result += 3
    elif w in "DEF":
        result += 4
    elif w in "GHI":
        result += 5
    elif w in "JKL":
        result += 6
    elif w in "MNO":
        result += 7
    elif w in "PQRS":
        result += 8
    elif w in "TUV":
        result += 9
    elif w in "WXYZ":
        result += 10
    else:
        result += 11


print(result)
