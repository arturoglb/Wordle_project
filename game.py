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
        self.BACKGROUND, self.WHITE,  = (0, 0, 0), (255, 255, 255)
        self.LETTER = (128, 128, 128)
        self.LETTER_IN_PLACE, self.LETTER_FOUND, self.LETTER_INCORRECT = (0, 255, 0), (255, 255, 0), (0, 0, 0)
        self.SELECTOR = (167, 73, 233)
        self.turn = 0
        self.board = [[" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " "]]
        self.fps = 30  # frame rate 30 frames per second
        self.timer = pygame.time.Clock()
        self.secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)]
        self.game_over = False
        self.letters = 0
        self.message = ""  # to add a message at the bottom of the screen
        self.turn_active = True
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def draw_board(self, size):
        font = pygame.font.Font(self.font_name, size)
        for col in range(0, 5):
            for row in range(0, 6):
                pygame.draw.rect(self.display, self.WHITE, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)  # squares around letter
                piece_text = font.render(self.board[row][col].upper(), True, self.LETTER)  # upper case when printing on screen
                self.display.blit(piece_text, (col * 100 + 30, row * 100 + 25))  # draw the text into the screen
        if not self.game_over:  # do not show selector if game is over
            pygame.draw.rect(self.display, self.SELECTOR, [5, self.turn * 100 + 5, self.DISPLAY_W - 10, 90], 3, 5)

    def draw_message(self):
        font = pygame.font.Font(self.font_name, 56)
        message_text = font.render(self.message, True, self.WHITE)
        self.display.blit(message_text, (40, 610))

    def check_words(self):
        for row in range(0, self.turn):
            # create secret word histogram: histogram[letter][index] = True
            secret_word_histogram = {}
            for col in range(0, 5):
                letter = self.secret_word[col]
                if not letter in secret_word_histogram:
                    secret_word_histogram[letter] = {}
                secret_word_histogram[letter][col] = True
            # build color array
            letter_colors = [self.LETTER_INCORRECT] * 5
            # check for in place letters
            for col in range(0, 5):
                letter = self.board[row][col]
                if letter in secret_word_histogram:
                    if col in secret_word_histogram[letter]:
                        letter_colors[col] = self.LETTER_IN_PLACE
                        secret_word_histogram[letter].pop(col)
                    if len(secret_word_histogram[letter].keys()) == 0:
                        secret_word_histogram.pop(letter)
            # check for found letters
            for col in range(0, 5):
                letter = self.board[row][col]
                if letter in secret_word_histogram:
                    if letter_colors[col] == self.LETTER_INCORRECT:  # stops yellow color from overriding green
                        letter_colors[col] = self.LETTER_FOUND
                        secret_word_histogram[letter].pop(next(iter(secret_word_histogram[letter])))
                    if len(secret_word_histogram[letter].keys()) == 0:
                        secret_word_histogram.pop(letter)
            # draw colors
            for col in range(0, 5):
                pygame.draw.rect(self.display, letter_colors[col], [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.timer.tick(self.fps)
            self.display.fill(self.BACKGROUND)
            self.check_words()
            self.draw_board(56)
            self.draw_message()
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False  # stop menu from running
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not self.playing or event.key == pygame.K_ESCAPE and self.playing:
                    self.START_KEY = True  # used to enter/exit game
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

            # Create the new screen for a new game
            if event.type == pygame.TEXTINPUT and self.turn_active and not self.game_over:
                entry = event.__getattribute__('text')  # text equal to a key to be shown
                if "a" <= entry.lower() <= "z":  # restrict to only letters
                    entry = entry.lower()
                    self.board[self.turn][self.letters] = entry
                    self.letters += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and self.letters > 0:
                    self.board[self.turn][self.letters - 1] = ' '  # Eliminate the letter that was entered
                    self.letters -= 1
                    self.message = ""

                if event.key == pygame.K_SPACE:  # CHEAT!! TO BE REMOVED IN FINAL PROGRAM
                    self.message = "".join(self.secret_word)

                if event.key == pygame.K_RETURN and self.game_over:  # to reset the game press return key
                    self.turn = 0
                    self.letters = 0
                    self.message = ""
                    self.game_over = False
                    self.secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)]
                    self.board = [[" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " "]]

                if event.key == pygame.K_RETURN and not self.game_over and self.letters == 5:  # restrict to 5 letters to move to next line
                    if self.in_wordlist():
                        # check if guess is correct, add game over conditions
                        guess = "".join(self.board[self.turn])
                        if guess == self.secret_word:
                            self.message = "You won! :-)"
                            self.game_over = True
                        elif self.turn == 5:
                            self.game_over = True
                            self.message = "You lost! :-("
                        self.turn += 1
                        self.letters = 0
                    else:
                        self.message = "Not in wordlist"

            # control turn active based on letters
            if self.letters == 5:
                self.turn_active = False
            if self.letters < 5:
                self.turn_active = True


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def in_wordlist(self):
        the_word = "".join(self.board[self.turn])
        return the_word in words.english_5L
