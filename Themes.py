import pygame

pygame.display.set_caption('Wordle with Add-ons')  # Title of the game
# backgrounds + to remove if possible
space = pygame.image.load('space.jpeg')
pokemon = pygame.image.load('pokemon.png')
nature = pygame.image.load('nature.jpeg')
pokemon_sc = pygame.transform.smoothscale(pokemon, (500, 700))
space_get = space.get_rect(topleft=(0, 0))
pokemon_get = pokemon_sc.get_rect(topleft=(0, 0))
nature_get = nature.get_rect(topleft=(0, 0))
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])

class backgrounds:
    def __init__(self, display):
        self.display = display
        self.keypressed = None
        self.state_bg = "color"

    def SetBG(self):  # adding chanching background
        if self.state_bg == "color":
            self.display.fill((0,0,0))
        else:
            if self.keypressed == pygame.K_1:
                self.display.blit(pokemon, (pokemon_get))
            if self.keypressed == pygame.K_2:
                self.display.blit(nature, (nature_get))
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
