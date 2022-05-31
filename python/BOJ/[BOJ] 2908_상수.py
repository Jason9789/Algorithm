A, B = map(str, input().split())

int_A = int(A[::-1])
int_B = int(B[::-1])


if int_A > int_B:
    print(int_A)
else:
    print(int_B)
