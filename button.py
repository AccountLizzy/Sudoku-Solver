import pygame
import subprocess

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.Font(None, 36) # You can choose a different font and size

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.color
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color

        pygame.draw.rect(surface, current_color, self.rect)

        text_surface = self.font.render(self.text, False, (0, 0, 0)) # Black text
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):  # Checks if button is clicked, and then run specified action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()



if __name__ == "__main__":
    subprocess.run(["python", "main.py"])

