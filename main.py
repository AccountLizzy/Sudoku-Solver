import pygame
import setup
from button import Button
import algorithm
import copy

# pygame setup
pygame.init()
pygame.display.set_caption('Sudoku Solver')
icon = pygame.image.load("window_icon.ico")
pygame.display.set_icon(icon)  # Set the window icon
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True
finish = False
error_msg = ""

grid_origin = [25, 10] # Top-left corner of the grid
cell_size = 65
pygame.font.init() # Initialize the font module
font = pygame.font.SysFont('Arial', 40) # Use for numbers
font2 = pygame.font.SysFont('Arial', 27) # Use for text
font3 = pygame.font.SysFont('Arial', 18)  # Use for credit
selected_number = None  # global variable
solved = False
flag = True

grid = [[1, None, None, 2, None, None, 4, None, None],
        [2, None, 3, None, None, None, None, None, None],
        [None, None, 4, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]]
temp_grid = []

class color:
    black = (0, 0, 0)
    dark_blue = (79, 148, 247)
    white = (255, 255, 255)
    red = (237, 111, 118)
    dark_red = (153, 11, 18)
    grey = (227, 227, 227)
    blue = (0, 192, 255)


#----------------------- BUTTON ACTIONS ------------------------#
def on_button_click(number):
    global finish, solved, selected_number, temp_grid, grid, flag, error_msg
    if number == 10:  # When "solve" clicked
        flag = True
        for row in range(9):
            for col in range(9):
                if grid[row][col] is not None:
                    number = grid[row][col]
                    grid[row][col] = None  # temporary remove
                    if not algorithm.checker(grid, row, col, number):
                        flag = False
                    grid[row][col] = number  # restore
                if flag == False:
                    break
            if flag == False:
                break
        if flag == False:
            error_msg = "Board not solvable"
        elif flag == True:
            temp_grid = copy.deepcopy(grid)
            algorithm.backtracker(grid, screen, font)
            finish = True
            selected_number = None
            solved = True
            flag = True
            error_msg = ""
    else:
        error_msg = ""
        if number == 11:  # When "reset" clicked
            solved = False
            for row in range(9):
                for col in range(9):
                    text_surface = font.render(str(grid[row][col]), False, (color.white))
                    x_cord = grid_origin[0] + col * cell_size
                    y_cord = grid_origin[1] + row * cell_size
                    screen.blit(text_surface, (x_cord, y_cord))  # Blit text at specified cords
            grid = [[None for _ in range(9)] for _ in range(9)]
        elif number == 12:  # del
            print(f"Button {number} clicked")
            selected_number = None
        else:
            selected_number = number
            print(f"Button {number} clicked")


# SETUP BUTTONS
button_1 = Button(625, 250, 75, 75, "1", (color.grey), (color.blue), lambda: on_button_click(1))
button_2 = Button(710, 250, 75, 75, "2", (color.grey), (color.blue), lambda: on_button_click(2))
button_3 = Button(795, 250, 75, 75, "3", (color.grey), (color.blue), lambda: on_button_click(3))
button_4 = Button(625, 335, 75, 75, "4", (color.grey), (color.blue), lambda: on_button_click(4))
button_5 = Button(710, 335, 75, 75, "5", (color.grey), (color.blue), lambda: on_button_click(5))
button_6 = Button(795, 335, 75, 75, "6", (color.grey), (color.blue), lambda: on_button_click(6))
button_7 = Button(625, 420, 75, 75, "7", (color.grey), (color.blue), lambda: on_button_click(7))
button_8 = Button(710, 420, 75, 75, "8", (color.grey), (color.blue), lambda: on_button_click(8))
button_9 = Button(795, 420, 75, 75, "9", (color.grey), (color.blue), lambda: on_button_click(9))
button_del = Button(625, 505, 75, 60, "Del", (color.grey), (153, 11, 18), lambda: on_button_click(12))
button_solve = Button(710, 505, 160, 60, "Solve", (161, 224, 240), (color.blue), lambda: on_button_click(10))
button_reset = Button(750, 10, 120, 30, "Reset", (color.red), (color.dark_red), lambda: on_button_click(11))

button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_solve, button_reset, button_del]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for btn in button_list:
            btn.handle_event(event) # Handle button events
        
        # Check mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:  # Click down
            mouse_x, mouse_y = event.pos
            if grid_origin[0] <= mouse_x <= grid_origin[0] + 9 * cell_size and \
               grid_origin[1] <= mouse_y <= grid_origin[1] + 9 * cell_size:
                
                col = (mouse_x - grid_origin[0]) // cell_size
                row = (mouse_y - grid_origin[1]) // cell_size
                print(f"Cell clicked: Row {row}, Column {col}, selected_number {selected_number}")

                grid[row][col] = selected_number
                

        # Screen set up 
        screen.fill("white")
        setup.set_up_board(screen=screen)
        screen.blit(font3.render("Project by Lizzy", True, (color.black)), (625, 18))

        # Add text
        if error_msg != "":
            selected_text = font2.render(error_msg, False, (color.red))
            screen.blit(selected_text, (625, 200))
        else:
            if selected_number is not None: 
                selected_text = font2.render(f"Selected number is: {selected_number}", False, (color.black))
            elif solved:
                selected_text = font2.render("Done! Reset to go again.", False, (color.black))
            else:
                selected_text = font2.render(f"Selected tool is: Eraser", False, (color.black))
            screen.blit(selected_text, (625, 200))

        # Update the text surface in grid array
        for row in range(9):
            for col in range(9):
                if grid[row][col] is not None: 
                    text_surface = font.render(str(grid[row][col]), False, (color.black))
                    x_cord = grid_origin[0] + col * cell_size
                    y_cord = grid_origin[1] + row * cell_size
                    screen.blit(text_surface, (x_cord, y_cord))  # Blit text at specified cords

        # Update text black when solved
        if solved:
            for row in range(9):
                for col in range(9):
                    if temp_grid[row][col] is not None: 
                        text_surface = font.render(str(temp_grid[row][col]), False, (color.dark_blue))
                        x_cord = grid_origin[0] + col * cell_size
                        y_cord = grid_origin[1] + row * cell_size
                        screen.blit(text_surface, (x_cord, y_cord))  # Blit text at specified cords
                    else:
                        continue


    # Button set up
    for btn in button_list:
        btn.draw(screen) # Draw the button

    clock.tick(60)  # limits FPS to 60
    pygame.display.update() # Update the display to show the changes

pygame.quit()