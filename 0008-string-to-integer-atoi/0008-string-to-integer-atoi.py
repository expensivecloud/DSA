class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sign = 1
        num = 0
        started = False

        for i in range(n):

            if s[i] == " " and not started:
                continue

            if (s[i] == "-" or s[i] == "+") and not started:
                if s[i] == "-":
                    sign = -1
                started = True
                continue

            if s[i].isdigit():
                started = True
                num = num * 10 + (ord(s[i]) - ord("0"))
            else:
                break

        num *= sign

        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num