class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        n = len(s)
        k = len(p)

        i = 0
        j = 0

        mp_p = {}
        mp_win = {}

        ans = []

        # Frequency of characters in p
        for ch in p:
            mp_p[ch] = mp_p.get(ch, 0) + 1

        while j < n:

            # Add s[j] to window
            mp_win[s[j]] = mp_win.get(s[j], 0) + 1

            # Window smaller than k
            if j - i + 1 < k:
                j += 1

            # Window size == k
            elif j - i + 1 == k:

                # Check if window is an anagram of p
                if mp_p == mp_win:
                    ans.append(i)

                # Remove s[i]
                mp_win[s[i]] -= 1

                if mp_win[s[i]] == 0:
                    del mp_win[s[i]]

                # Slide window
                i += 1
                j += 1

        return ans