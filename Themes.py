import pygame

pygame.display.set_caption('Wordle with Add-ons')  # Title of the game
# backgrounds + to remove if possible
space = pygame.image.load('space.jpeg')
pokemon2 = pygame.image.load('pokemon2.jpg')
lightning = pygame.image.load('lightning.jpg')
space_get = space.get_rect(topleft=(0, 0))
pokemon_get = pokemon2.get_rect(topleft=(-150, 0))
lightning_get= lightning.get_rect(topleft=(-850, -300))
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])

class backgrounds:
    def __init__(self, display):
        self.display = display
        self.keypressed = None
        self.state_bg = "color"

    def SetBG(self):  # adding changing background
        if self.state_bg == "color":
            self.display.fill((0,0,0))
        else:
            if self.keypressed == pygame.K_1:
                self.display.blit(pokemon2, (pokemon_get))
            if self.keypressed == pygame.K_2:
                self.display.blit(lightning, (lightning_get))
            if self.keypressed == pygame.K_3:
                self.display.blit(space, (space_get))

    def check_key_entry(self,key):
        if key == pygame.K_1:  # add background if press 1 test
            self.keypressed = pygame.K_1
            self.state_bg = 'img'
        if key == pygame.K_2:
            self.keypressed = pygame.K_2
            self.state_bg = 'img'
        if key == pygame.K_3:
            self.keypressed = pygame.K_3
            self.state_bg = 'img'
        if key == pygame.K_4:
            self.keypressed = pygame.K_4
            self.state_bg = 'color'
