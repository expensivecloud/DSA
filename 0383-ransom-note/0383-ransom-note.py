class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mp = {}

        for i in range(len(magazine)):
            mp[magazine[i]] = mp.get(magazine[i], 0) + 1

        for i in range(len(ransomNote)):
            ch = ransomNote[i]

            if ch not in mp or mp[ch] == 0:
                return False

            mp[ch] -= 1

        return True