from ntpath import join
from typing import Counter


n = int(input())

dp = []

for i in range(1, n+1):
    tmp = []

    for n in str(i):
        if n == "3" or n == "6" or n == "9":
            tmp.append('-')

        else:
            tmp.append(n)

    cnt = Counter(tmp)
    if cnt and cnt['-'] == 1:
        dp.append('-')
    elif cnt and cnt['-'] == 2:
        dp.append('--')

    else:
        dp.append(''.join(tmp))


print(' '.join(dp))
