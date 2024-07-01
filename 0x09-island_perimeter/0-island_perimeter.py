#!/usr/bin/python3
"""
Perimeter of an island
"""
def island_perimeter(grid):
  """
  Determine the perimeter of an island.
  
  Args:
  the perimeter of the island described in grid
  
  Returns:
  0 represents water
  1 represents land
  Each cell is square, with a side length of 1
  Cells are connected horizontally/vertically (not diagonally).
  grid is rectangular, with its width and height not exceeding 100
  """
  if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four directions
                # Up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
