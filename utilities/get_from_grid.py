def grid_get(grid, x, y, default = "."):
    if x < 0 or y < 0:
        return default
    try:
        return grid[y][x]
    except IndexError:
        return default
    
# If grid is out of bounds will return a '.'