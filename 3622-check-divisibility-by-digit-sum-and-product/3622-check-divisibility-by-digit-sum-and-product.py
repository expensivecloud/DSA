class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """

        n_list = str(n)

        digit_sum = 0
        digit_product = 1

        for digit in n_list:
            d = int(digit)

            digit_sum += d
            digit_product *= d

        total = digit_sum + digit_product

        return n % total == 0