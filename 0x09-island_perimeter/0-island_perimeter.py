#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
    grid (list of list of int): 2D list representing the island, where 0 is water and 1 is land.
    
    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the land cell
                perimeter += 4
                # Subtract 1 for each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1
    
    return perimeter
