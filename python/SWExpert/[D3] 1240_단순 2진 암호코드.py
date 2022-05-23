code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = []
    binary = ''

    for i in range(N):
        arr.append(input())

        if not binary and '1' in arr[i]:
            binary = arr[i]

    p = M - binary[::-1].index('1')
    binary = binary[p-56:p]

    num = []

    for i in range(0, 56, 7):
        num.append(code[binary[i:i+7]])

    odd = 0
    even = 0
    result = 0

    for i in range(8):
        if i == 7:
            if (odd * 3 + even + num[i]) % 10 == 0:
                result = odd + even + num[i]

            else:
                result = 0
        elif i % 2:
            even += num[i]
        else:
            odd += num[i]

    print(f'#{tc} {result}')
