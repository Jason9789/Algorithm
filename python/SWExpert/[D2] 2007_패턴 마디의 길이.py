t = int(input())

for i in range(1, t+1):
    str = input()

    for j in range(1, 10):
        if str[:j] == str[j:2*j]:
            print(f'#{i} {j}')
            break
