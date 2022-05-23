for tc in range(1, 11):
    T = int(input())
    word = input()
    words = input()

    cnt = 0

    for i in range(len(words)):
        tmp = ""
        if words[i] == word[0]:
            tmp += words[i:i+len(word)]
            if tmp == word:
                cnt += 1

    print(f'#{tc} {cnt}')
