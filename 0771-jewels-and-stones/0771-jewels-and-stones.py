class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        jewel_set = set(jewels)

        res = 0

        for stone in stones:
            if stone in jewel_set:
                res += 1

        return res