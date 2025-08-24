import pygame
import subprocess
from button import Button


def set_up_board(screen):
    # SETUP BOARD PHASE 1
    for column in (67, 134, 267, 334, 467, 534):
        pygame.draw.rect(screen, "grey", (column, 0, 1, 600))  # (left, top, width, height)
    for row in (67, 134, 267, 334, 467, 534):
        pygame.draw.rect(screen, "grey", (0, row, 600, 1))

    # SETUP BOARD PHASE 2
    for column in (0, 200, 400, 600):
        pygame.draw.rect(screen, "black", (column, 0, 3, 600))  # (left, top, width, height)
    for row in (0, 200, 400, 597):
        pygame.draw.rect(screen, "black", (0, row, 600, 3))

    

if __name__ == "__main__":
    subprocess.run(["python", "main.py"])