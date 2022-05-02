# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         results = []
#         window = collections.deque()
#         current_max = float('-inf')

#         for i, v in enumerate(nums):
#             window.append(v)

#             if i < k - 1:
#                 continue

#             # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
#             if current_max == float('-inf'):
#                 current_max = max(window)

#             elif v > current_max:
#                 current_max = v

#             results.append(current_max)

#             # 최대값이 윈도우에서 빠지면 초기화
#             if current_max == window.popleft():
#                 current_max = float('-inf')

#         return results

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        sol = []
        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()
            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)
            if i >= k - 1:
                sol.append(nums[q[0]])
        return sol
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         results = []
#         window = collections.deque()
#         current_max = float('-inf')

#         for i, v in enumerate(nums):
#             window.append(v)

#             if i < k - 1:
#                 continue

#             # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
#             if current_max == float('-inf'):
#                 current_max = max(window)

#             elif v > current_max:
#                 current_max = v

#             results.append(current_max)

#             # 최대값이 윈도우에서 빠지면 초기화
#             if current_max == window.popleft():
#                 current_max = float('-inf')

#         return results


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        sol = []
        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()
            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)
            if i >= k - 1:
                sol.append(nums[q[0]])
        return sol
