class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        for s in jewels:
            for r in stones:
                if r == s:
                    res+=1

        return res