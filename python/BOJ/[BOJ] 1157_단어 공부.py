from typing import Counter


word = input().lower()


counter_word = Counter(word)

if len(counter_word) > 1 and counter_word.most_common(2)[0][1] == counter_word.most_common(2)[1][1]:
    print("?")
else:
    print(counter_word.most_common(1)[0][0].upper())
