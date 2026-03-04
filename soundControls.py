import pygame
from button import Button
import config
from button import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

class SoundControls:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Semi-transparent background for submenu
        self.submenu_bg = pygame.Surface((500, 210))  # Smaller than the full screen
        self.submenu_bg.set_alpha(180)  # Semi-transparent
        self.submenu_rect = self.submenu_bg.get_rect(center=(config.WIN_WIDTH // 2, config.WIN_HEIGHT // 2))
        stars_image = pygame.image.load('Images/backgrounds/space-stars.png')
        self.bg_stars = pygame.transform.scale(stars_image, (WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 24)

        # init vars for background movement
        self.bg_stars_x1 = 0
        self.bg_stars_x2 = WIN_WIDTH

        button_y_start = 100  # Starting y-position of the first button
        self.exitButton = Button((300, button_y_start + 500), (200, 50), WHITE, 'Return')

    def run(self):
        # Initialize and draw the slider
        slider_x = self.submenu_rect.x + 50
        slider_y = self.submenu_rect.y + 60
        slider_w = self.submenu_bg.get_width() - 100
        slider = Slider(self.screen, slider_x, slider_y, slider_w, 20, min=0, max=99, step=1)
        output = TextBox(self.screen, slider_x + (slider_w // 2) - 15, slider_y + 80, 30, 30, fontSize=21)

        while self.running:
            events = pygame.event.get()
            for event in events:
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
            self.screen.blit(self.submenu_bg, self.submenu_rect) # Show the submenu screen with the slider

            output.disable()  # Act as label instead of textbox
            output.setText(slider.getValue())

            pygame_widgets.update(events)
            pygame.display.update()

    def update_background(self):
        self.bg_stars_x1 -= 1  # Adjust speed as necessary
        self.bg_stars_x2 -= 1

        # Reset positions to loop the background
        if self.bg_stars_x1 + WIN_WIDTH < 0:
            self.bg_stars_x1 = WIN_WIDTH

        if self.bg_stars_x2 + WIN_WIDTH < 0:
            self.bg_stars_x2 = WIN_WIDTH
