
# 입력
n = int(input())
stocks = [int(x) for x in input().strip().split()]

# stocks를 돌면서 그 순간의 사는 가격, 파는 가격, 최대 이익을 저장해놓는다.
# 모든 상황을 저장하여 최종 결과값을 도출해낸다.
result = list()

minPrice = stocks[0]
maxPrice = stocks[0]

# 최대값과 최솟값 index를 통해서 최대이익이 있는 경우와 없는 경우를 나타낼 예정이다.
minPriceIndex = 0
maxPriceIndex = 0

for stock in range(1, len(stocks)):

    profit = stocks[stock]

    # profit이 기존의 maxProfit 보다 클 경우 maxProfit을 profit으로 데이터 갱신
    if maxPrice < profit:
        maxPrice = profit
        maxPriceIndex = stock

    # profit이 기존의 minProfit 보다 작을 경우 minProfit을 profit으로 데이터 갱신.
    elif minPrice > profit:
        # result list에 최대 이익, 사는 가격, 파는 가격을 저장한다.
        result.append((maxPrice - minPrice, minPrice, maxPrice))

        # minPrice와 MaxPrice를 현재 profit으로 다시 갱신 시킨다.
        minPrice = profit
        maxPrice = profit

        # Index 또한 현재의 index로 초기화 시킨다.
        minPriceIndex = stock
        maxPriceIndex = stock

# for문 종료 시 최종적인 값들을 result 배열에 넣는다.
result.append((maxPrice - minPrice, minPrice, maxPrice))

# 최대 이익으로 정렬하며, 최대 이익이 같을시, 사는 가격이 낮은 순으로 정렬한다.
result_sorted = sorted(result, key=lambda x: (-x[0], x[1]))

# 최대 파는 가격의 인덱스보다 최소 파는 가격의 인덱스가 작은 경우는 최대 이익이 없는 경우이다.
if maxPriceIndex <= minPriceIndex:
    print(-1)
else:
    print(result_sorted[0][2] - result_sorted[0][1])
    print(result_sorted[0][1], result_sorted[0][2])
