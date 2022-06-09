import sys
input = sys.stdin.readline

n = int(input())

solution = list(map(int, input().split()))
solution.sort()

result = float('inf')
left, right = 0, n-1
mix = []

while left < right:
    total = solution[left] + solution[right]

    if abs(total) < result:
        result = abs(total)
        mix = [solution[left], solution[right]]

    if total < 0:
        left += 1

    else:
        right -= 1

print(mix[0], mix[1])
