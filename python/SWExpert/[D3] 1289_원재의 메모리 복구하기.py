T = int(input())

for tc in range(1, T+1):
    memory = list(input())

    bits = ['0'] * len(memory)
    cnt = 0

    for i in range(len(memory)):
        if bits[i] != memory[i]:
            cnt += 1
            bits[i:] = memory[i] * len(bits[i:])

    print(f'#{tc} {cnt}')
