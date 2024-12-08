from rich.console import Console
from rich.text import Text

def visualize_grid(grid, guides_on=False, green_char_array=[], blue_coord_array=[]):
    
    console = Console()
    display_grid = [row.copy() for row in grid]
    
    # coordinate guides
    if guides_on:
        # Create column headers
        col_headers = ['*'] + list(range(len(display_grid[0])))
        display_grid.insert(0, col_headers)
        
        # Add row numbers
        for i in range(1 if guides_on else 0, len(display_grid)):
            display_grid[i].insert(0, i-1 if guides_on else i)
    
    # Determine the maximum width needed for any cell
    def get_cell_width(grid):
        if guides_on:
            row_label_width = len(str(len(grid) - 1))
        else:
            row_label_width = 0
        
        content_width = max(max(len(str(cell)) for cell in row) for row in grid)
        
        # Can Adjust Padding
        return max(row_label_width, content_width) + 2  
    
    
    # Calculate cell width dynamically
    cell_width = get_cell_width(display_grid)
    
    for y, row in enumerate(display_grid):
        formatted_row = []
        for x, cell in enumerate(row):
            # Create a Rich Text object to handle colors properly
            text_cell = Text(str(cell).center(cell_width))
            
            # Styling
            if guides_on and  y == 0:
                text_cell.stylize("yellow")

            if guides_on and x == 0:
                text_cell.stylize("yellow")
            
            if ((guides_on) and (x > 0) and (y > 0) and (cell in green_char_array)) or ((guides_on==False) and (cell in green_char_array)):
                    text_cell.stylize("bold green")

            if guides_on and blue_coord_array and [y-1, x-1] in blue_coord_array:
                text_cell.stylize("bold bright_cyan")

            elif not guides_on and blue_coord_array and [y, x] in blue_coord_array:
                text_cell.stylize("bold bright_cyan")
            
            formatted_row.append(text_cell)
        
        console.print(Text().join(formatted_row))

# Example Usage

# map = [['a','b','c','d'],
# ['a','b','c','d'],
# ['a','b','c','d'],
# ['a','b','c','d']]

# visualize_grid(map)
# visualize_grid(map,True)
# visualize_grid(map,True,['a','c'])
# visualize_grid(map,True,['a','c'],[[0,1],[1,3],[2,1],[3,3]])


