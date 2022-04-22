# import your modules
import random
import pygame
import words
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Optional
pygame.init()

# create screen, fonts, colors, game variables
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
gray = (128, 128, 128)
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # crerate the screen setup
pygame.display.set_caption('Wordle with Add-ons') # Title of the game
turn = 0 # show on the screen what turn you on
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]] # matrix created (number of spaces 5 letters)

fps = 60 # frame rate 60 frames per second
timer = pygame.time.Clock()
huge_font = pygame.font.Font('freesansbold.ttf', 56) # define the font you like for the game
secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)] # choose a random word from a list
game_over = False
letters = 0
turn_active = True # verify if you have completed all spaces with letters

# create routine for drawing the board

def draw_board():
    global turn
    global board
    for col in range(0, 5):
        for row in range(0, 6):
            pygame.draw.rect(screen, white, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5) # how the rectangles look on the screen
            piece_text = huge_font.render(board[row][col], True, gray) # how the text will appear on the game per row and column
            screen.blit(piece_text, (col * 100 + 30, row * 100 + 25)) # draw the text into the screen
    pygame.draw.rect(screen, green, [5, turn * 100 + 5, WIDTH - 10, 90], 3, 5) # create rectangle to show on which turn you at

# create routine for checking letters

def check_words():
    global turn
    global board
    global secret_word
    for col in range(0, 5):
        for row in range(0, 6):
            if secret_word[col] == board[row][col] and turn > row: # Checking if the word is equal to the one wrote by player after pressed enter
                pygame.draw.rect(screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5) # create green rectangle if it guess a letter
            elif board[row][col] in secret_word and turn > row:
                pygame.draw.rect(screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5) # create green rectangle if it guess a letter


# set up your main game loop

running = True
while running:
    timer.tick(fps)
    screen.fill(black) # screen background
    check_words() # goes before draw_board if not letters are behind color squares
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # get out of the game (infinite loop)
            running = False
# add player controls for letter entry, backspacing, checking guesses and restarting

        if event.type == pygame.TEXTINPUT and turn_active and not game_over: # grab text that is press from the keyboard
                entry = event.__getattribute__('text')  # text equal to a key to be shown
                if entry != " ":
                    entry = entry.lower()
                    board[turn][letters] = entry
                    letters += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turn][letters - 1] = ' '  # Eliminate the letter that was entered
                letters -= 1
            if event.key == pygame.K_SPACE and not game_over:
                turn += 1
                letters = 0
            if event.key == pygame.K_SPACE and game_over:
                turn = 0
                letters = 0
                game_over = False
                secret_word = words.english_5L[random.randint(0, len(words.english_5L) - 1)]
                board = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

        # control turn active based on letters
        if letters == 5:
            turn_active = False
        if letters < 5:
            turn_active = True

        # check if guess is correct, add game over conditions

        for row in range(0, 6):
            guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
            if guess == secret_word and row < turn:
                game_over = True

        if turn == 6:
            game_over = True
            loser_text = huge_font.render('Loser!', True, white) # Create the Loser text at the bottom
            screen.blit(loser_text, (40, 610))

        if game_over and turn < 6:
            winner_text = huge_font.render('Winner!', True, white) # Create the Winner text at the bottom
            screen.blit(winner_text, (40, 610))


    pygame.display.flip()
pygame.quit()