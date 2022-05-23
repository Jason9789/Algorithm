mirror = {
    'b': 'd',
    'd': 'b',
    'q': 'p',
    'p': 'q'
}

T = int(input())

for tc in range(1, T+1):
    case = input()
    result = ""

    for i in case:
        result += mirror[i]

    print(f'#{tc} {result[::-1]}')
