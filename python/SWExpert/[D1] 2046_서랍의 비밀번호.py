p, k = input().split()

p = int(p)
k = int(k)

result = 0

if p < k:
    result = p - k + 1001

else:
    result = p - k + 1

print(result)
