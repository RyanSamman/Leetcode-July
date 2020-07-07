class Solution:
    def __init__(self):
        self.grid = [[0]]
        self.height = 0
        self.width = 0

    def islandPerimeter(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

        perimeter = 0
        # i is height j is width
        for i in range(0, self.height):
            for j in range(0, self.width):
                perimeter += self.getCorners(i, j)

        return perimeter

    def getCorners(self, i, j):
        if not self.grid[i][j]:
            return 0

        corners = 4

        if i - 1 >= 0:
            corners -= 1 if self.grid[i - 1][j] else 0
        if i + 1 < self.height:
            corners -= 1 if self.grid[i + 1][j] else 0
        if j - 1 >= 0:
            corners -= 1 if self.grid[i][j - 1] else 0
        if j + 1 < self.width:
            corners -= 1 if self.grid[i][j + 1] else 0

        return corners


if __name__ == '__main__':
    array = [[1]]
    x = Solution()
    print(x.islandPerimeter(array))
