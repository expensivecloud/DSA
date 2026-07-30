class Solution(object):
    def setZeroes(self, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])

        row_zeros = set()
        col_zeros = set()


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0
