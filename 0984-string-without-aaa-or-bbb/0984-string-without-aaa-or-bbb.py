class Solution(object):
    def strWithout3a3b(self, a, b):
        s = []

        while a > 0 or b > 0:

            # If last two are same, we MUST use the other character
            if len(s) >= 2 and s[-1] == s[-2]:
                if s[-1] == 'a':
                    s.append('b')
                    b -= 1
                else:
                    s.append('a')
                    a -= 1

            # Otherwise use the character with more remaining
            elif a > b:
                s.append('a')
                a -= 1

            else:
                s.append('b')
                b -= 1

        return "".join(s)