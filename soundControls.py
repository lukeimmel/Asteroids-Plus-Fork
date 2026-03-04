import pygame
from button import Button
import config
from button import *

class SoundControls:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Semi-transparent background for submenu
        self.submenu_bg = pygame.Surface((500, 600))  # Smaller than the full screen
        self.submenu_bg.fill((50, 50, 50))  # Dark grey background
        self.submenu_bg.set_alpha(180)  # Semi-transparent
        self.submenu_rect = self.submenu_bg.get_rect(center=(config.WIN_WIDTH // 2, config.WIN_HEIGHT // 2))
        stars_image = pygame.image.load('Images/backgrounds/space-stars.png')
        self.bg_stars = pygame.transform.scale(stars_image, (WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 24)

        # Semi-transparent background for submenu
        self.message_box = pygame.Surface((340, 500))  # Smaller width, enough for text
        self.message_box.fill((50, 50, 50))  # Dark grey background
        self.message_box.set_alpha(180)  # Semi-transparent
        self.message_box_rect = self.message_box.get_rect(topright=(WIN_WIDTH - 50, 100))
        self.current_message = None  # Store the current message to display

        # init vars for background movement
        self.bg_stars_x1 = 0
        self.bg_stars_x2 = WIN_WIDTH

        button_y_start = 100  # Starting y-position of the first button
        self.exitButton = Button((300, button_y_start + 500), (200, 50), WHITE, 'Return')

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exitButton.is_clicked(event):
                        self.running = False

            self.update_background()
            self.screen.fill((0, 0, 0))  # Clear the screen or fill with base color
            self.screen.blit(self.bg_stars, (self.bg_stars_x1, 0))
            self.screen.blit(self.bg_stars, (self.bg_stars_x2, 0))
            self.exitButton.draw(self.screen, BLACK)


            pygame.display.update()

    def update_background(self):
        self.bg_stars_x1 -= 1  # Adjust speed as necessary
        self.bg_stars_x2 -= 1

        # Reset positions to loop the background
        if self.bg_stars_x1 + WIN_WIDTH < 0:
            self.bg_stars_x1 = WIN_WIDTH

        if self.bg_stars_x2 + WIN_WIDTH < 0:
            self.bg_stars_x2 = WIN_WIDTH