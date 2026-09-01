class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0

        for ch in s:
            ans ^= ord(ch)

        for ch in t:
            ans ^= ord(ch)

        return chr(ans)
        