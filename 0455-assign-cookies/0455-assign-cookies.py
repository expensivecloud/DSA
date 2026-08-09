class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n = len(g)
        g.sort()
        m = len(s)
        s.sort()

        cnt = 0
        l,r = 0,0

        while l < n and r < m:
            if g[l] <= s[r]:
                cnt += 1
                l += 1
                r += 1
            else:
                r += 1

        return cnt