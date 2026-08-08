class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        n = len(s2)
        k = len(s1)

        if k > n:
            return False

        mp_s1 = {}
        mp_win = {}

        # Frequency map of s1
        for ch in s1:
            mp_s1[ch] = mp_s1.get(ch, 0) + 1

        i = 0
        j = 0

        while j < n:

            # Add current character
            mp_win[s2[j]] = mp_win.get(s2[j], 0) + 1

            # Window smaller than k
            if j - i + 1 < k:
                j += 1

            # Window size == k
            elif j - i + 1 == k:

                # Permutation found
                if mp_s1 == mp_win:
                    return True

                # Remove leftmost character
                mp_win[s2[i]] -= 1

                if mp_win[s2[i]] == 0:
                    del mp_win[s2[i]]

                # Slide
                i += 1
                j += 1

        return False