# 파이썬 코딩테스트 팁

## 입출력 방법

1. 입출력

   `input()`, `print()` 를 사용하다보면 종종 시간 초과가 난다. 그렇기에 조금이라도 단축하려면 다음과 같은 방법을 사용한다.

   ```python
   import sys
   n = int(sys.stdin.readline())
   ```

   이 조차도 귀찮으면

   ```python
   from sys import stdin, stdout

   input = stdin.readline
   print = stdout.write

   n = int(input())
   print(n)
   ```

   이때, 주의할 점

   - 문자열을 입력 받을 땐 `strip()` 넣기 (넣지 않으면 `\n` 까지 같이 입력 받음.)

   <br/>
   <br/>

2. 배열 입력 받기 (초기화)

   - 1차원 리스트

     ```python
     arr = [0] * n
     ```

   - 2차원 리스트 n \* m

     ```python
     arr = [[0] * m for _ in range(n)]
     ```

   - 2차원 배열 입력 받기

     ```python
     arr = [list(map(int, input().split())) for _ in range(n)]
     ```

   - 문자열을 한 글자씩 배열에 저장할 때
     ```python
     arr = [list(input()) for _ in range(n)]
     ```

<br>
<br>

---

## 최대값 최솟값 정의

```python
import sys

max_value = sys.maxsize
min_value = sys.minsize

max_value = float('inf')
min_value = float('int')

```

<br>
<br>

---

## 리스트에서 index, value를 함께 출력

```python
for i, v in enumerate(list):
  print(i, v)
```

<br>
<br>

---

## 딕셔너리

```python
a = dict()

a = {}
```

위와 같이 표현할 수 있다. 또한 다음과 같이 선언 가능하다

```python
a = {'key1': 'value1', 'key2': 'value2'}
print(a) # {'key1': 'value1', 'key2': 'value2'}

a['key3'] = 'value3'
print(a) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3' }

a['key1'] # 'value1'
```

단, `dict()` 혹은 `{}`로 선언한 **딕셔너리**는 리스트에서 존재하지 않는 인덱스를 조회활 경우 `IndexError`가 발생한다.

`try` 구문 혹은 `if` 문으로 예외 처리가 가능하다

```python
try:
  print(a['key4'])
except KeyError:
  print('존재하지 않는 키')

if 'key4' in a:
  print('존재')
else:
  print('존재 하지 않음')
```

### 딕셔너리 모듈

`defaultdict` 객체를 사용하게 되면 예외처리를 하지 않아도 된다.

즉, 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로 해딩 카에 대한 딕셔너리 아이템을 생성해준다.

```python
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a) # defaultdict(<class 'int'>, {'A': 5, 'B': 4})
```

<br>
<br>

---

## 자주 쓰이는 리스트 관련 함수

- `append()` : 원소 삽입 `O(1)`
- `sort()` : 오름차순 정렬 `O(NlogN)`
- `sort(reverse=True)` : 내림차순 정렬 `O(NlogN)`
- `sort(key=lambda x:(x[0], x[1]))` : 첫 번째 요소를 기준으로 정렬하고, 첫번째 요소가 같을 때, 두 번째 요소를 기준으로 정렬한다.
- `insert(index, value)` : 특정 인덱스 위치에 원소 삽입 `O(N)`
- `count(value)` : 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용 `O(N)`
- `remove(value)` : 특정 값을 갖는 원소를 제거한다. 값을 가진 원소가 여러개면 하나만 제거한다 `O(N)`

리스트를 쓸 때에 리스트 앞뒤로 자료를 추가하거나 뺄 필요가 있다면 리스트보다 `deque()`을 사용하는 것이 좋다.

<br>
<br>

---

## 진법 계산

1. 10진수 -> 2, 8, 16진수

   ```python
   bin(42) # 'ob101010'
   oct(42) # '0o52'
   hex(42) # '0x2a'
   ```

2. 2, 8, 16진수 -> 10진수
   ```python
   int('0b111100', 2) # 60
   int('0o74', 8)     # 60
   int('0x3c', 16)    # 60
   ```

<br>
<br>

---

## 문자열

1. 문자열 뒤집기

   ```python
   word = "abcd"
   word[::-1]  # "dcba"
   ```

2. 아스키 코드 변환
   ```python
   print (ord('A'))  # 65
   print(chr(65))    # A
   ```

<br>
<br>

---

## 리스트 변환 (문자열 변환)

1. 문자열 -> 리스트

   ```python
   num_str = "1,3,2"
   print(num_str.split(',')) # ['1', '3', '2']
   ```

2. 리스트 -> 문자열
   ```python
   num_list = ['1', '3', '2']
   print(' '.join(num_list)) # 1 2 3
   ```

<br>
<br>

---

## 재귀를 코드에서 사용할 때 필수

```python
import sys
sys.setrecursionlimit(10 ** 6)
```

<br>
<br>

---

## 조합

```python
from itertools import combinations

print(list(combination([1, 2, 3, 4], 3)))
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```

<br>
<br>

---

## 순열

```python
from itertools import permutations

print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

<br>
<br>

---

## 힙

1. 최소 힙

   - 루트가 가장 작은 값으로 이루어진 힙
   - 파이썬의 `heapq`는 최소 힙으로 구현되어 있음.

     ```python
       import heapq

       heap = []
       heapq.heappush(heap, 3)
       heapq.heappush(heap, 1)
       heapq.heappush(heap, 10)
       heapq.heappush(heap, 5)
       heapq.heappush(heap, 8)
       heapq.heappush(heap, 6)

       print(heap)
       # [1, 3, 6, 5, 8, 10]

       heapq.heappop(heap)
       print(heap)
       # [3, 6, 5, 8, 10]``
     ```

2. 최대 힙

   - 루트가 가장 큰 값으로 이루어진 힙
   - 입력할 때 -1을 곱해서 `heap`에 넣고 출력할 때 -1을 곱해서 출력하는 식으로 구할 수 있음

     ```python
         # 예시입니다.

           import heapq

           heap = []
           heapq.heappush(heap, -3)
           heapq.heappush(heap, -1)
           heapq.heappush(heap, -10)
           heapq.heappush(heap, -5)
           heapq.heappush(heap, -8)
           heapq.heappush(heap, -6)

           print(heap)
           # [-10, -8, -6, -1, -5, -3]

           print(heapq.heappop(heap) * -1)
           # 10
     ```

<br>
<br>

---

## `deque`

- 큐나 스택을 사용할 때 쓰면 좋음.
- 덱은 양방향에서 데이터 처리 가능

  ```python
  from collections import deque

  de = deque()

  de.append(10)
  de.appendleft(10)

  de.pop()
  de.popleft()
  ```

<br>
<br>

---

## 빈도 계산

```python
from collections import Counter

arr = [1, 1, 1, 2, 2, 3, 4, 5]

counter = Counter(arr).most_common()
print(counter)
# [(1, 3), (2, 2), (3, 1), (4, 1), (5, 1)]
```
