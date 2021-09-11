# 주식 투자를 즐기는 홍길동은 n일 동안 어떤 회사의 주식을 다음과 같이 매매한다:
# 주식 한 주를 한 번만 사서 이를 다음에 한 번 팔 수 있다.
# 홍길동은 n일 동안 주식 매매(한번 사서 한번 판다)를 하여 얻은 이익에 대하여, 얻을 수 있는 최대 이익과 얼마나 차이가 있는지를 알고 싶어한다.
# 그래서 이 기간 동안 얻을 수 있는 최대 이익을 계산하기로 하였다.
# 예를 들어, 7일 동안 주식 가격이 (30, 25, 50, 10, 20, 40)과 같을 때,
# 최대 이익은 네째 날 주식을 사서 마지막 날 팔면 이익이 30(=40–10)이다.
# n일 동안 주식 가격이 주어질 때, 얻을 수 있는 최대 이익을 구하는 프로그램을 작성하시오.

# 입력 형식
# 첫째 줄에는 n이 주어진다. n은 2 이상 100,000 이하의 정수이다.
# 둘째 줄에는 주식 가격(양의 정수)이 날짜 순서대로 n개 주어진다.
# -----
# 15
# 6 5 10 5 7 9 25 1 4 10 6 23 5 3 12 2 4 24 14 10

# 10
# 20 19 18 17 16 10 9 8 7 6

# 출력 형식
# 최대 이익을 첫 번째 줄에 출력한다.
# 두 번째 줄에 사는 가격과 파는 가격을 각각 출력한다.
# 최대 이익을 얻는 경우가 여러 개일 때는, 사는 가격이 최소인 경우 하나만 출력한다.
# 이득이 없는 경우는, –1만 출력한다.
# -----
# 23
# 1 24

# -1

print("주식 프로그램")

# 최대 이익을 구하는 함수
def maxProfit(n, stocks):
    minPrice = stocks[0]    # 최소 사는 가격을 stocks[0]으로 초기화
    maxProfit = 0           # 최대 이익 초기화
    result = []             # 최종 결과 저장 배열

    day = 1                 # minPrice로 매수한 시점부터 n일 동안 매매를 한다.
    stock = 1               # 주어진 주식 날짜에서의 하루를 의미한다. 하루가 지날 때마다 +1 된다.

    # 입력 받은
    while stocks:
        # 그 날의 이익을 담아두는 변수
        profit = stocks[stock] - minPrice

        # 최대 이익보다 당일 이익이 크다면 최대 이익 변수의 값을 갱신
        if profit > maxProfit:
            maxProfit = profit

        # 다음 날의 주식 가격이 최소 가격보다 작다면 갱신
        # 최소 가격이 갱신되면 그 날부터 다시 n번일 동안 매매를 하기에 day 변수를 1로 초기화
        if stocks[stock] < minPrice:
            minPrice = stocks[stock]
            day = 1
            continue

        # 최소 가격이 갱신되지 않는다면 매매 일수 변수(day)와 총 매매 일수(stock)을 +1 해준다.
        day += 1
        stock += 1

        # day가 n이 되지 않았는데 stock 변수가 입력받은 총 매매일수보다 커졌을 경우 break
        if stock > len(stocks) - 1:
            break

        # n일 동안 주식 매매 종료 시점
        if day == n:
            break

    # 이익이 없으면 -1
    if maxProfit <= 0:
        result.append(-1)
        return result

    # 이익이 있으면 최대 이익, 사는 가격, 파는 가격을 반환한다.
    else:
        maxPrice = maxProfit + minPrice
        for i in [maxProfit, minPrice, maxPrice]:
            result.append(i)

        return result



# 입력
n = int(input())
stocks = [int(x) for x in input().strip().split()]

# maxProfit 함수를 통한 최종 결과 배열을 저장
resultList = maxProfit(n, stocks)

# 배열의 길이가 1이면 이득이 없는 경우이기에 -1 출력
# 배열의 길이가 1 이상이면 이득이 있기에 최대 이익, 사는 가격, 파는 가격을 출력한다.
if len(resultList) == 1:
    print(resultList[0])
else:
    print(resultList[0])
    print(resultList[1], resultList[2])