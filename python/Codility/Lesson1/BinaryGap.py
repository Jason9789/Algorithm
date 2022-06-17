# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    bin_n = list(bin(N)[2:])
    # print(bin_n)

    dist = [0] * (len(bin_n) + 1)
    cnt = 1

    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            dist[i] = cnt-1
            cnt = 1

        else:
            cnt += 1

    max_gap = max(dist)

    return max_gap
