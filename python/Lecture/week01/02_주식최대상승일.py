
print("주식 최대 상승일")

# 입력
n = int(input())
stocks = [int(x) for x in input().strip().split()]

continuousRiseIndex = []            # 연속하여 지수가 오른 날들의 배열
maxIndex = 0                        # continuousRiseIndex의 길이
result = 0                          # 연속하여 지수가 오른 날 수의 최대 값

# stocks[n]과 stocks[n+1]을 비교하기 위하여 0부터 len(stocks)-1까지 반복
for stock in range(0, len(stocks)-1):
    continuousRiseIndex.append(stocks[stock])

    # n보다 n+1의 값이 더 클 때
    if stocks[stock] < stocks[stock+1]:
        # maxIndex 값 갱신
        maxIndex = len(continuousRiseIndex)

        # result 값보다 maxIndex의 값이 클 때 값 갱신
        if result <= maxIndex:
            result = maxIndex

    # n이 n+1보다 작을 때, continuousRiseIndex 배열 초기화
    else:
        continuousRiseIndex.clear()


print(result)