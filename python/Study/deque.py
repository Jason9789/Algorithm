from collections import deque

a = [1, 2, 3, 4, 5]

q = deque(a)                    # deque([1, 2, 3, 4, 5])

print(f'a : {a}')
print(f'q : {q}')

q.rotate(2)  # 2만큼 우측으로 회전. 만약 좌측 회전이면 -2 입력

result = list(q)

print(f'q: {q}')                # deque([4, 5, 1, 2, 3])
print(f'result : {result}')
print()

# deque는 list와 비슷한데, appendleft와 popleft가 사용 가능하다.

d = deque(a)
d.append(6)                     # d : deque([1, 2, 3, 4, 5, 6])

print(f'd : {d}')

d.appendleft(0)                 # d : deque([0, 1, 2, 3, 4, 5, 6])
print(f'd : {d}')

d.popleft()
print(f'd : {d}')
