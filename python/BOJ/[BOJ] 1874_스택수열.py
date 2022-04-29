

n = int(input())

count = 0
stack = []
result = []
sequence = True

for _ in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")

    if x == stack[-1]:
        stack.pop()
        result.append("-")

    else:
        sequence = False


print("\n".join(result)) if sequence else print("NO")
