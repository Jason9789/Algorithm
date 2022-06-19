import sys
input = sys.stdin.readline

S = input().strip()
result = []

for i in range(len(S)):
    for j in range(len(S)-i):
        result.append(S[j:j+i+1])

print(len(set(result)))
