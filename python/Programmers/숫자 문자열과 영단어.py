def solution(s):
    answer = []

    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    num = ""
    for i in s:
        num += str(i)
        if num in numbers:
            answer.append(numbers[num])
            num = ""

        if i.isdigit():
            answer.append(int(i))
            num = ""

    return int(''.join(map(str, answer)))
