import heapq
import math
from pprint import pprint

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

h = []  # 힙 생성

# for문으로 heapq에 저장하기
for score in data:
    heapq.heappush(h, score)    # 힙에 데이터 저장

print("\n우수 3명 : for")
for i in range(3):
    print(heapq.heappop(h))     # 최솟값부터 힙 반환


# 혹은
heapq.heapify(data)             # data 자체를 힙 구조에 맞게 변경한다.

print("\n우수 3명 : heapify")
for i in range(3):
    print(heapq.heappop(data))  # 최솟값부터 힙 반환


# pprint -> 복잡한 구조를 지닌 json 데이터를 디버깅 용도로 출력할 때 자주 사용
print("\npprint")
pprint(data)


# math 라이브러리

print(math.factorial(5))
print(math.sqrt(6))
print(math.gcd(35, 14))
print(math.pi)
print(math.e)
