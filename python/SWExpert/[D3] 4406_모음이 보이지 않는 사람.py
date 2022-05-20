vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())

for tc in range(1, T+1):
    word = input()

    new_word = ''

    for w in word:
        if w in vowel:
            continue
        else:
            new_word += w

    print(f'#{tc} {new_word}')
