# Animations added to wordle
# -----------------------------------------
# packages
import pygame
import os
import random

# -----------------------------------------

# pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % (150, 50)

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Flame Particles using Pygame')

FPS = 60

clock = pygame.time.Clock()


class FlameParticle:  # grey particules
    alpha_layer_qty = 2
    alpha_glow_difference_constant = 2

    def __init__(self, x=150, y=250, r=5):
        self.x = x
        self.y = y
        self.r = r
        self.original_r = r
        self.alpha_layers = FlameParticle.alpha_layer_qty
        self.alpha_glow = FlameParticle.alpha_glow_difference_constant
        max_surf_size = 2 * self.r * self.alpha_layers * self.alpha_layers * self.alpha_glow
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        self.burn_rate = 0.1 * random.randint(1, 4)

    def update(self):
        self.y -= 5 - self.r
        self.x += random.randint(-self.r, self.r)
        self.original_r -= self.burn_rate
        self.r = int(self.original_r)
        if self.r <= 0:
            self.r = 1

    def draw(self, window):
        max_surf_size = 2 * self.r * self.alpha_layers * self.alpha_layers * self.alpha_glow
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        for i in range(self.alpha_layers, -1, -1):
            alpha = 255 - i * (255 // self.alpha_layers - 5)
            if alpha <= 0:
                alpha = 0
            radius = self.r * i * i * self.alpha_glow
            if self.r == 4 or self.r == 3:
                r, g, b = (255, 0, 0)
            elif self.r == 2:
                r, g, b = (255, 150, 0)
            else:
                r, g, b = (50, 50, 50)
            # r, g, b = (0, 0, 255)  # uncomment this to make the flame blue
            color = (r, g, b, alpha)
            pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), radius)
        window.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))


class Flame:
    def __init__(self, x=550, y=650):
        self.x = x
        self.y = y
        self.flame_intensity = 2
        self.flame_particles = []
        for i in range(self.flame_intensity * 25):
            self.flame_particles.append(FlameParticle(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))

    def draw_flame(self, window):
        for i in self.flame_particles:
            if i.original_r <= 0:
                self.flame_particles.remove(i)
                self.flame_particles.append(FlameParticle(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))
                del i
                continue
            i.update()
            i.draw(window)

    def check_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                quit()

    def launchAnimation(self, window):
        # while True:
        events = pygame.event.get()
        self.check_events(events)
        s = self.flame_particles[0]
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(self.x - 50, self.y - 150, 120, 250)) # remove BLACK rect
        self.draw_flame(window)
        pygame.display.update()
        clock.tick(15)

# main_window()
