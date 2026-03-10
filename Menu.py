import pygame
from AsteroidsRound import *
from shipSelectScreen import *
from button import *
from leaderboard import *
from instructions import *
from CoOp import *
import pygame.font
import config
from soundControls import SoundControls


class Menu:
    def __init__(self):
        pygame.init()
        self.title = "Asteroids   Plus"
        self.title_font = pygame.font.Font('Galaxus-z8Mow.ttf', 100)
        self.title_text = self.title_font.render(self.title, True, WHITE)
        self.title_y = 150
        self.title_y_velocity = 0.20
        # load screen and images for background
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.background = pygame.image.load('Images/backgrounds/space-backgound.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))
        stars_image = pygame.image.load('Images/backgrounds/space-stars.png')
        self.bg_stars = pygame.transform.scale(stars_image, (WIN_WIDTH, WIN_HEIGHT))
        self.shipicon = pygame.image.load('Images/ships/ship-a/ship-a-damaged.png')
        self.volume = INITIAL_VOLUME

        # init vars for background movement
        self.bg_stars_x1 = 0
        self.bg_stars_x2 = WIN_WIDTH
        # init clock for FPS
        self.clock = pygame.time.Clock()

        self.running = True
        self.playButton = Button((WIN_WIDTH/2 - 130, WIN_HEIGHT/2 - 150), (100, 100), WHITE, "PLAY")
        self.shipSelect = Button((WIN_WIDTH/2 - 130, WIN_HEIGHT/2), (100, 100), WHITE, "SHIP", 'Images/ships/ship-a/ship-a-damaged.png')
        self.exitButton = Button((WIN_WIDTH / 2 + 20, WIN_HEIGHT / 2 + 150), (100, 100), WHITE, "EXIT")
        self.statButton = Button((WIN_WIDTH/2 -50, WIN_HEIGHT/2 + 300), (100, 100), WHITE, "STATS")
        self.instructionsButton = Button((WIN_WIDTH - 120, WIN_HEIGHT - 70), (100, 50), WHITE, "Help")
        self.soundButton = Button((20, WIN_HEIGHT - 70), (100, 50), WHITE, "Sound")
        self.coOpButton = Button((WIN_WIDTH/2 + 20, WIN_HEIGHT/2 - 150), (100, 100), WHITE, "CO-OP")
        self.bgButton = Button((WIN_WIDTH/2 + 20, WIN_HEIGHT/2), (100, 50), WHITE, "BG")
        self.starsButton = Button((WIN_WIDTH/2 + 20, WIN_HEIGHT/2 + 50), (100, 50), WHITE, "STARS")
        #New cheater/sandbox mode - Jack
        self.cheaterButton = Button((WIN_WIDTH / 2 - 130, WIN_HEIGHT / 2 + 150), (100, 100), WHITE, "CHEAT")

        # Bg File
        self.backgrounds = [
            'Images/backgrounds/space-backgound.png',
            'Images/backgrounds/Space Bg 1.png',
            # 'Images/backgrounds/',
        ]
        self.bg_index = 0
        self.selected_bg = self.backgrounds[0]

        # Star file
        self.stars_options = [
            'Images/backgrounds/space-stars.png',
            'Images/backgrounds/Space Star.png',
            # 'Images/backgrounds/',
        ]
        self.stars_index = 0
        self.selected_stars = self.stars_options[0]

    def change_background(self):
        self.bg_index = (self.bg_index + 1) % len(self.backgrounds)
        self.selected_bg = self.backgrounds[self.bg_index]
        self.background = pygame.image.load(self.selected_bg).convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))

    def change_stars(self):
        self.stars_index = (self.stars_index + 1) % len(self.stars_options)
        self.selected_stars = self.stars_options[self.stars_index]
        stars_image = pygame.image.load(self.selected_stars)
        self.bg_stars = pygame.transform.scale(stars_image, (WIN_WIDTH, WIN_HEIGHT))

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.bg_stars, (self.bg_stars_x1 ,0))
        self.screen.blit(self.bg_stars, (self.bg_stars_x2 ,0))

        self.title_y += self.title_y_velocity
        if self.title_y >= WIN_HEIGHT - 635:
            self.title_y = WIN_HEIGHT - 635
            self.title_y_velocity = -0.20
        elif self.title_y <= 150:
            self.title_y = 150
            self.title_y_velocity = 0.20

        title_rect = self.title_text.get_rect(center=(WIN_WIDTH/2, self.title_y))
        self.screen.blit(self.title_text, title_rect)

        self.clock.tick(FPS)
        pygame.mouse.set_visible(True)

        self.playButton.draw(self.screen, BLACK)
        self.shipSelect.draw(self.screen, BLACK)
        self.exitButton.draw(self.screen, BLACK)
        self.statButton.draw(self.screen, BLACK)
        self.instructionsButton.draw(self.screen, BLACK)
        self.soundButton.draw(self.screen, BLACK)
        self.coOpButton.draw(self.screen, BLACK)
        self.bgButton.draw(self.screen, BLACK)
        self.starsButton.draw(self.screen, BLACK)
        self.cheaterButton.draw(self.screen, BLACK)

        pygame.display.update()

    def update_background(self):
        # Move backgrounds to the left
        self.bg_stars_x1 -= 1
        self.bg_stars_x2 -= 1

        if self.bg_stars_x1 + WIN_WIDTH < 0:
            self.bg_stars_x1 = WIN_WIDTH

        if self.bg_stars_x2 + WIN_WIDTH < 0:
            self.bg_stars_x2 = WIN_WIDTH

    def show_instructions(self):
        inst_menu = InstructionsMenu(self.screen)
        inst_menu.run()

    def update_volume(self):
        config.MUSIC_CHANNEL.set_volume(self.volume)
        config.ASTEROID_CHANNEL.set_volume(self.volume)
        config.PLAYER_CHANNEL.set_volume(self.volume)
        config.PLAYER_DESTROYED_CHANNEL.set_volume(self.volume)
        config.SHIP_CHANNEL.set_volume(self.volume)
        config.POWERUP_CHANNEL.set_volume(self.volume)

    def show_sound_controls(self):
        sound_controls = SoundControls(self.screen, self.volume)
        self.volume = sound_controls.run()
        self.update_volume()

    def play(self):
        self.update_volume()
        selected_ship = 0
        while True:
            m.draw()
            m.update_background()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

                if self.playButton.is_clicked(event):
                    g = Game(selected_ship, self.selected_bg, self.selected_stars, cheat_mode=False)
                    g.new()
                    while g.running:
                        g.main()
                if self.cheaterButton.is_clicked(event):
                    g = Game(selected_ship, self.selected_bg, self.selected_stars, cheat_mode=True)
                    g.new()
                    while g.running:
                        g.main()

                if self.shipSelect.is_clicked(event):
                    select = ShipSelection()
                    selected_ship = select.main()
                    while select.running:
                        select.main()

                if self.instructionsButton.is_clicked(event):
                    self.show_instructions()

                if self.soundButton.is_clicked(event):
                    self.show_sound_controls()

                if self.statButton.is_clicked(event):
                    leaderboard = LeaderBoard()
                    while leaderboard.running:
                        leaderboard.view()

                if self.coOpButton.is_clicked(event):
                    c = CoOp(selected_ship, self.selected_bg, self.selected_stars)
                    c.new()
                    while c.running:
                        c.main()

                if self.bgButton.is_clicked(event):
                    self.change_background()

                if self.starsButton.is_clicked(event):
                    self.change_stars()

                if self.exitButton.is_clicked(event):
                    pygame.quit()
                    exit()


m = Menu()
while m.running:
    m.play()