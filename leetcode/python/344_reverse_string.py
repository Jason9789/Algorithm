from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(s)
        s.reverse()
        print(s)


sol = Solution()
sol.reverseString(["h","e","l","l","o"])