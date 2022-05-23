T = int(input())

for tc in range(1, T+1):
    num = input()

    if int(num[-1]) % 2 == 0:
        print(f'#{tc} Even')
    else:
        print(f'#{tc} Odd')
