class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):

        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = []
            rows[r].append(c)

        # Rows with no reservations can fit 2 families
        ans = (n - len(rows)) * 2

        for r in rows:

            block1 = True
            block2 = True
            block3 = True

            for c in rows[r]:

                if c in [2, 3, 4, 5]:
                    block1 = False

                if c in [4, 5, 6, 7]:
                    block2 = False

                if c in [6, 7, 8, 9]:
                    block3 = False

            if block1 and block3:
                ans += 2

            elif block1 or block2 or block3:
                ans += 1

        return ans