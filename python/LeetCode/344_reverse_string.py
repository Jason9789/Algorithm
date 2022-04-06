from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


# Input
S = Solution()

input = list(map(str, input().split()))
print(input)

S.reverseString(input)
