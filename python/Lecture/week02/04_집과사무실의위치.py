
import heapq

roads = []
result = 0

# 입력 부분
n = int(input())

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] < tmp[1]:
        roads.append([tmp[1], tmp[0]])
    else:
        roads.append(tmp)

d = int(input())

# 도착 지점을 기준으로 road list를 정렬해준다.
roads.sort(key=lambda x: x[1])

heap = []

# for road in roads:
#     if not heap:
#         heapq.heappush(heap, road)
#
#     else:
#         while heap[0][0] < road[1] - d:
#             heapq.heappop(heap)
#
#             if not heap:
#                 break
#         heapq.heappush(heap, road)
#
#     result = max(result, len(heap))
#
# print(result)