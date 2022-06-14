from collections import deque
import sys
read = sys.stdin.readline

n = int(read())

de = deque()

for _ in range(n):
    cmd = read().split()

    if cmd[0] == 'push_back':
        de.append(cmd[1])

    elif cmd[0] == 'push_front':
        de.appendleft(cmd[1])

    elif cmd[0] == 'pop_front':
        if de:
            print(de.popleft())
        else:
            print(-1)

    elif cmd[0] == 'pop_back':
        if de:
            print(de.pop())
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(de))

    elif cmd[0] == 'empty':
        if de:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if de:
            print(de[0])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if de:
            print(de[-1])
        else:
            print(-1)
