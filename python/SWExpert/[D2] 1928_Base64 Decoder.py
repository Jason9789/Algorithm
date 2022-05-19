# from base64 import b64decode

# T = int(input())

# for tc in range(1, T+1):
#     base64 = input()

#     res = b64decode(base64).decode('UTF-8')

#     print(f'#{tc} {res}')


# 라이브러리 사용 X
decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ]

T = int(input())

for tc in range(1, T+1):
    word = list(input())

    res = ''

    for i in range(len(word)):
        num = decode.index(word[i])
        bin_num = str(bin(num)[2:])

        while len(bin_num) < 6:
            bin_num = '0' + bin_num

        res += bin_num

    r = ''

    for w in range(len(word)*6//8):
        e = int(res[w*8:w*8+8], 2)
        r += chr(e)

    print('#{} {}'.format(tc, r))
