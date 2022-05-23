# mirror = {
#     'b': 'p',
#     'd': 'q',
#     'q': 'd',
#     'p': 'b'
# }

T = int(input())

for tc in range(1, T+1):
    case = input()
    result = ""

    for i in case:
        result += i

    print(f'#{tc} {result[::-1]}')
