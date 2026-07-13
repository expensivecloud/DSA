class Solution(object):
    def topKFrequent(self, nums, k):
        hmap = {}

        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        freq = sorted(hmap, key=hmap.get, reverse=True)

        return freq[:k]