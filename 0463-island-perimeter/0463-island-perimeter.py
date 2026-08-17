class Solution(object):
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        per = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    per += 4

                    if row > 0 and grid[row-1][col] == 1:
                        per -= 1
                    if row < rows - 1 and grid[row+1][col] == 1:
                        per -= 1
                    if col > 0 and grid[row][col-1] == 1:
                        per -= 1
                    if col < cols - 1 and grid[row][col+1] == 1:
                        per -= 1

        return per