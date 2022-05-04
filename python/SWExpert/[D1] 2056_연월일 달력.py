# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 22220228

T = int(input())

for i in range(1, T+1):
    year = ""
    month = ""
    day = ""

    flag = True

    tmp = input()

    # 년 판별
    if int(tmp[0:4]) > -1:
        year = tmp[0:4]
    else:
        flag = False

    # 월 판별
    if int(tmp[4:6]) > 0 and int(tmp[4:6]) < 13:
        month = tmp[4:6]
    else:
        flag = False

    # 일 판별
    if flag:
        int_month = int(month)

    if int_month == 1 or int_month == 3 or int_month == 5 or int_month == 7 or int_month == 8 or int_month == 10 or int_month == 12:
        if int(tmp[6:]) > 0 and int(tmp[6:]) < 31:
            day = tmp[6:]

        else:
            flag = False

    elif int_month == 4 or int_month == 6 or int_month == 9 or int_month == 11:
        if int(tmp[6:]) > 0 and int(tmp[6:]) < 30:
            day = tmp[6:]

        else:
            flag = False

    else:
        if int(tmp[6:]) > 0 and int(tmp[6:]) <= 28:
            day = tmp[6:]
        else:
            flag = False

    if flag:
        print('#{0} {1}/{2}/{3}'.format(i, year, month, day))
    else:
        print('#{0} -1'.format(i))


# 5
# 22220228
# 20150002
# 01010101
# 20140230
# 11111111

   # 1 2222/02/28
#2 -1
# 3 0101/01/01
#4 -1
# 5 1111/11/11
