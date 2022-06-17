from collections import Counter
from itertools import count


n = int(input())
card = list(map(int, input().split()))

m = int(input())
deck = list(map(int, input().split()))

counter = Counter(card)

card = set(card)

for d in deck:
    if d in card:
        print(counter[d], end=" ")

    else:
        print("0", end=" ")
