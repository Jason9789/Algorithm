import sys
input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))

m = int(input())
deck = list(map(int, input().split()))


for d in deck:
    if d in card:
        print(1, end=" ")

    else:
        print(0, end=" ")
