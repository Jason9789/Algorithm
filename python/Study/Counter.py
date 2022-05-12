from collections import Counter


def countLetters(word):
    counter = {}

    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1

    return counter


print(countLetters('Hello world'))


# Counter 함수 사용
print(Counter('hello world'))
print(Counter('hello world').most_common(1))
