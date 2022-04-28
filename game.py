from menu import *
import random
import pygame
import words
import pygame_menu


pygame.display.set_caption('Wordle with Add-ons') # Title of the game


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 500, 700
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame_menu.font.FONT_NEVIS
        self.BLACK, self.WHITE,  = (0, 0, 0), (255, 255, 255)
        self.GREEN, self.YELLOW, self.GRAY = (0, 255, 0), (255, 255, 0), (128, 128, 128)
        self.turn = 0
        self.board = [[" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "]]
        self.fps = 60  # frame rate 60 frames per second
        self.timer = pygame.time.Clock()
        self.secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)]
        self.game_over = False
        self.letters = 0
        self.turn_active = True
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def draw_board(self, size):
        font = pygame.font.Font(self.font_name, size)
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(self.display, self.WHITE, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)
                piece_text = font.render(self.board[row][col], True, self.GRAY)
                self.display.blit(piece_text, (col * 100 + 30, row * 100 + 25))  # draw the text into the screen
        pygame.draw.rect(self.display, self.GREEN, [5, self.turn * 100 + 5, self.DISPLAY_W - 10, 90], 3, 5)

    def check_words(self):
        for col in range(0, 5):
            for row in range(0, 6):
                if self.secret_word[col] == self.board[row][col] and self.turn > row:
                    pygame.draw.rect(self.display, self.GREEN, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
                elif self.board[row][col] in self.secret_word and self.turn > row:
                    pygame.draw.rect(self.display, self.YELLOW, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.timer.tick(self.fps)
            self.display.fill(self.BLACK)
            self.check_words()
            self.draw_board(56)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False # stop menu from running
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

            # Create the new screen for a new game
            if event.type == pygame.TEXTINPUT and self.turn_active and not self.game_over:
                entry = event.__getattribute__('text')  # text equal to a key to be shown
                if entry != " ":
                    entry = entry.lower()
                    self.board[self.turn][self.letters] = entry
                    self.letters += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and self.letters > 0:
                    self.board[self.turn][self.letters - 1] = ' '  # Eliminate the letter that was entered
                    self.letters -= 1
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.turn += 1
                    self.letters = 0
                if event.key == pygame.K_SPACE and self.game_over:
                    self.turn = 0
                    self.letters = 0
                    self.game_over = False
                    self.secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)]
                    self.board = [[" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "]]

            # control turn active based on letters
            if self.letters == 5:
                self.turn_active = False
            if self.letters < 5:
                self.turn_active = True

            # check if guess is correct, add game over conditions
            for row in range(0, 6):
                guess = self.board[row][0] + self.board[row][1] + self.board[row][2] + self.board[row][3] +\
                        self.board[row][4]
                if guess == self.secret_word and row < self.turn:
                    self.game_over = True

            if self.turn == 6:
                self.game_over = True
                font = pygame.font.Font(self.font_name, 56)
                loser_text = font.render('Loser!', True, self.WHITE)
                self.display.blit(loser_text, (40, 610))

            if self.game_over and self.turn < 6:
                font = pygame.font.Font(self.font_name, 56)
                winner_text = font.render('Winner!', True, self.WHITE)  # Create the Winner text at the bottom
                self.display.blit(winner_text, (40, 610))

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
