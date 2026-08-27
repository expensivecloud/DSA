class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        chs = set()
        ans = 0

        while right < len(s):
            if s[right] in chs:
                chs.remove(s[left])
                left += 1
            else:
                chs.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1

        return ans