'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

class Solution(object):
    def islandPerimeter(self, grid):
        length = 0
        for r in range(len(grid)):
            for c in range(len(grid[-1])):
                if grid[r][c] == 1:
                    up = 1 if r == 0 or grid[r - 1][c] == 0 else 0
                    down = 1 if r == len(grid) - 1 or grid[r + 1][c] == 0 else 0
                    left = 1 if c == 0 or grid[r][c - 1] == 0 else 0
                    right = 1 if c == len(grid[-1]) - 1 or grid[r][c + 1] == 0 else 0
                    length += (up + down + left + right)
        return length

s = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(Solution().islandPerimeter(s))
