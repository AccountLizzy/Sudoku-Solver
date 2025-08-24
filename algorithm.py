from itertools import permutations
import pygame

def square_finder(index):
    if 0 <= index < 3:
        return 0
    if 3 <= index < 6:
        return 1
    if 6 <= index < 9:
        return 2




# check if number can go to cell (by checking row col and square)
def checker(grid, row, col, number):  # Procedure return bool
    # Check against row and col
    for i in range(9):
        if number == grid[row][i] or number == grid[i][col]:
            return False
        else:
            continue

    # Check against square
    rw = square_finder(row) * 3
    cl = square_finder(col) * 3
    for r in range(rw, rw + 3):
        for c in range(cl, cl + 3):
            if number == grid[r][c]:
                return False
            else:
                continue

    
    # Return true (number is good) if not return false
    return True
    

# scan to find another empty cell
def finder(grid):  # Procedure return row and col
    for row in range(9):
        for col in range(9):
            if grid[row][col] is None:
                return (row, col)
            elif row == 9 and col == 9 and grid[row][col] is not None:
                return None, None  # SOLVED


possible_numbers = [_ for _ in range(1, 10)]  # Initialize / reset 

# retrace step (the engine)
def backtracker(grid, screen, font):

    # 1. Find an empty cell to work on
    cell = finder(grid)
    if cell is None and cell is None:
        return True  # solved
    
    # 2. Put an available number onto the empty cell
    for number in possible_numbers:
        if checker(grid, cell[0], cell[1], number):
            grid[cell[0]][cell[1]] = number
            text_surface = font.render(str(number), False, (0, 0, 0))
            screen.blit(text_surface, (cell[1], cell[0]))
            if backtracker(grid, screen, font): # Recurse to ensure this number wont cause problem for next number
                return True
            grid[cell[0]][cell[1]] = None  # backtrack to go higher


    # 3. backtrack higher if nothing worked
    return False

