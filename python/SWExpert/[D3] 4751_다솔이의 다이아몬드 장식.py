T = int(input())

for tc in range(1, T+1):
    word = input()

    # 첫 줄
    print("..", end='')
    if len(word) == 1:
        print("#", end='')
    else:
        for i in range(len(word)):
            print("#", end='')

            if i != len(word)-1:
                print("...", end='')
    print("..")

    # 두 번째
    print(".", end='')
    print("#." * len(word)*2)

    # 세 번째
    print("#", end='')

    for i in range(len(word)):
        print(f'.{word[i]}.#', end='')
    print()

    # 네 번째
    print(".", end='')
    print("#." * len(word)*2)

    # 다섯 번째
    print("..", end='')
    if len(word) == 1:
        print("#", end='')
    else:
        for i in range(len(word)):
            print("#", end='')

            if i != len(word)-1:
                print("...", end='')
    print("..")
