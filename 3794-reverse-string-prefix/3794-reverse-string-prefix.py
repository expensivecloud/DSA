class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        re = []

        for i in range(k):
            re.append(s[i])

        re_s = "".join(re)

        n_s = s[k:]

        return re_s[::-1] + n_s