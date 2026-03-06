import pygame
from config import *

class Button(object):

    def __init__(self, position, size, color, text, image_path=None):
        
        self.input_text = text
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 32)

        # Always load the border image as the button background
        self.border_image = pygame.image.load('Images/button.png').convert_alpha()

        if image_path:
            # If a custom image is passed (e.g. ship select), use that instead
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, size)
        else:
            # Use the border image scaled to button size
            self.image = pygame.transform.scale(self.border_image, size)

        self.rect = pygame.Rect((0, 0), size)

        if text:
            self.text = self.font.render(self.input_text, False, WHITE)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.rect.center
            self.image.blit(self.text, self.text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen, color):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # Hovered - slightly brightened border
            hovered = pygame.transform.scale(self.border_image, self.rect.size)
            bright = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            bright.fill((60, 60, 60, 100))
            hovered.blit(bright, (0, 0))
            self.text = self.font.render(self.input_text, False, WHITE)
            hovered.blit(self.text, self.text_rect)
            screen.blit(hovered, self.rect)
        else:
            # Normal - just the border image
            normal = pygame.transform.scale(self.border_image, self.rect.size)
            self.text = self.font.render(self.input_text, False, WHITE)
            normal.blit(self.text, self.text_rect)
            screen.blit(normal, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)