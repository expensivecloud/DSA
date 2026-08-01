class Solution(object):
    def reverseWords(self, s):

        n = len(s)
        res = []

        i = 0

        while i < n:

            while i < n and s[i] == " ":
                i += 1

            word = []

            while i < n and s[i] != " ":
                word.append(s[i])
                i += 1

            if word:
                res.append("".join(word))

        res.reverse()

        return " ".join(res)
        