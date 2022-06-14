# from collections import deque
# from distutils.log import error
# import sys
# read = sys.stdin.readline

# t = int(read())

# for _ in range(t):
#     cmd = read()
#     length = int(read())
#     arr = read()

#     if length > 0:
#         arr = arr[1:-2]
#         arr = list(map(int, arr.split(',')))
#     else:
#         print("error")
#         continue

#     de = deque(arr)

#     for c in cmd:
#         if c == "R":
#             de.reverse()

#         if c == "D":
#             if not de:
#                 print("error")

#             else:
#                 de.popleft()

#     if de:
#         print(list(de))

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


# input
t = int(input())

for _ in range(t):
    cmd = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    cmd = cmd.replace('RR', '')
    de = deque()

    for i in arr:
        if i != '':
            de.append(i)

    cnt = 0
    flag = 0

    for i in cmd:
        if i == "R":
            cnt += 1

        elif i == "D":
            if len(de) == 0:

                flag = 1  # 에러일 때.
                break

            else:
                if cnt % 2 == 0:
                    de.popleft()
                else:
                    de.pop()

    if flag == 1:
        print("error")
    else:
        if cnt % 2 == 1:
            de.reverse()

        print("[", end='')
        for i in range(len(de)):
            if i == len(de) - 1:
                print(de[i], end='')
            else:
                print(str(de[i]) + ",", end='')
        print("]")
