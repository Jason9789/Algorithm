import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # freqs = collections.Counter(nums).most_common(k)

        # # print(freqs)
        # return [f[0] for f in freqs]

        return list(zip(*collections.Counter(nums).most_common(k)))[0]
