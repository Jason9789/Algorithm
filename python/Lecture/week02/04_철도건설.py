
import heapq

temp_roads = []
roads = []
result = 0

# 입력 부분
n = int(input())

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] > tmp[1]:
        temp_roads.append([tmp[1], tmp[0]])
    else:
        temp_roads.append(tmp)

d = int(input())

for temp_road in temp_roads:
    if abs(temp_road[0] - temp_road[1]) <= d:
        roads.append(temp_road)

# 도착 지점을 기준으로 road list를 정렬해준다.
roads.sort(key=lambda x: x[1])
# print("temp roads :", temp_roads)
# print("roads :", roads)

# 힙 만들어주기
heap = []

# 입력받은 roads list를 반복하여 체크한다.
for road in roads:
    # 힙이 비어있으면 road의 값을 push 한다.
    if not heap:
        heapq.heappush(heap, road)

    # 힙이 비어있지 않을 때,
    else:
        # 힙의 가장 작은 값이 철로 안에 존재하지 않으면 힙에서 제외한다.
        while heap[0][0] < road[1] - d:
            # print("heap :", heap)
            # print("heap[0][0] :", heap[0][0])
            # print("road :", road)
            # print("road[1] :", road[1])
            heapq.heappop(heap)

            # 힙이 비어있으면 멈춘다.
            if not heap:
                break

        # road의 시작과 끝점의 차이가 d보다 크면 d에 포함할 수 없다.
        # 그러니 road의 차이가 d보다 작은 것들만 힙에 저장한다.
        # if abs(road[0] - road[1]) <= d:
        heapq.heappush(heap, road)

    # if result < len(heap):
    #     print("heap :", heap)

    # d에 최대로 들어갈 수 있는 값들을 비교하며 result를 갱신한다.
    result = max(result, len(heap))

print(result)