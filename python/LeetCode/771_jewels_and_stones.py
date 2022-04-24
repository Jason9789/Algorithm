class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        count = 0

        for s in stones:
            if s not in freq:
                freq[s] = 1

            else:
                freq[s] += 1

        for j in jewels:
            if j in freq:
                count += freq[j]

        return count
