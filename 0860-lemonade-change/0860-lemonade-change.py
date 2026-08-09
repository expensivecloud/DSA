class Solution(object):
    def lemonadeChange(self, bills):
        cnt5 = 0
        cnt10 = 0

        for bill in bills:

            if bill == 5:
                cnt5 += 1

            elif bill == 10:
                if cnt5 == 0:
                    return False

                cnt10 += 1
                cnt5 -= 1

            elif bill == 20:
                if cnt10 > 0 and cnt5 > 0:
                    cnt10 -= 1
                    cnt5 -= 1
                elif cnt5 >= 3:
                    cnt5 -= 3
                else:
                    return False

        return True