class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        words.sort(key=len)

        n = len(words)
        dp = [1] * n

        def compare(str1, str2):
            if len(str2) != len(str1) + 1:
                return False

            i = 0
            j = 0

            while i < len(str1) and j < len(str2):
                if str1[i] == str2[j]:
                    i += 1

                j += 1

            return i == len(str1)

        for i in range(n):
            for j in range(i):
                if compare(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)