class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        i = 0
        j = 0

        vowels = ['a','e','i','o','u']
        max_cnt = 0
        cnt = 0

        while j<n:

            if s[j] in vowels:
                cnt += 1

            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                if cnt > max_cnt:
                    max_cnt = cnt
                
                if s[i] in vowels:
                    cnt -= 1
                i+=1
                j+=1

        return max_cnt


