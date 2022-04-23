# import heapq

# heap = []
# heapq.heappush(heap, 50)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)

# # print(heap)

# result = heapq.heappop(heap)
# # print("result: {result} \nheap: {heap}")

# # print(heap[0])
# # print(heap)

# # 미리 생성한 리스트는 heapify 함수를 통해 힙으로 변환 가능.
# heap2 = [50, 10, 20, 30]
# heapq.heapify(heap2)
# # print(heap2)


# # ==============
# # 최대힙
# # ==============
# heap_items = [1, 3, 5, 7, 9]

# max_heap = []
# for item in heap_items:
#     heapq.heappush(max_heap, (-item, item))

# print(max_heap)


from collections import deque

priorities = [2, 1, 3, 2]

queue = deque((v, i) for i, v in enumerate(priorities))

print(queue)
print(max(queue))
