import pygame

import words


class Menu():
    def __init__(self, game): # include a reference to game object because there are functions that we want to reuse
        self.game = game # to get access to the function already created in game.py
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True # tell our menu to run
        self.cursor_rect = pygame.Rect(0, 0, 20, 20) # (x,y,w,h)
        self.offset = - 100 # position of the cursor on the menu

    def draw_cursor(self):
        self.game.draw_text('#', 15, self.cursor_rect.x, self.cursor_rect.y) # create the cursor

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu): # inherit menu class
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start" # so the cursor can be present at the "Start Game" option
        self.startx, self.starty = self.mid_w, self.mid_h + 30 # position in the middle of screen with adding to height
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # assign a start position to the cursor

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BACKGROUND) # reset the screen
            self.game.draw_text('Main Menu', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Start Game', 30, self.startx, self.starty)
            self.game.draw_text('Options', 30, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Difficulty'
        self.difficultyx, self.difficultyy = self.mid_w, self.mid_h + 30
        self.lengthx, self.lengthy = self.mid_w, self.mid_h + 60
        self.languagex, self.languagey = self.mid_w, self.mid_h + 90
        self.themex, self.themey = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.difficultyx + self.offset, self.difficultyy) # assign a start position to the cursor

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Difficulty', 30, self.difficultyx, self.difficultyy)
            self.game.draw_text('Word Length', 30, self.lengthx, self.lengthy)
            self.game.draw_text('Language', 30, self.languagex, self.languagey)
            self.game.draw_text('Theme', 30, self.themex, self.themey)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Difficulty':
                self.cursor_rect.midtop = (self.lengthx + self.offset, self.lengthy)
                self.state = 'Word Length'
            elif self.state == 'Word Length':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Language'
            elif self.state == 'Language':
                self.cursor_rect.midtop = (self.themex + self.offset, self.themey)
                self.state = 'Theme'
            elif self.state == 'Theme':
                self.cursor_rect.midtop = (self.difficultyx + self.offset, self.difficultyy)
                self.state = 'Difficulty'
        elif self.game.UP_KEY:
            if self.state == 'Difficulty':
                self.cursor_rect.midtop = (self.themex + self.offset, self.themey)
                self.state = 'Theme'
            elif self.state == 'Theme':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Language'
            elif self.state == 'Language':
                self.cursor_rect.midtop = (self.lengthx + self.offset, self.lengthy)
                self.state = 'Word Length'
            elif self.state == 'Word Length':
                self.cursor_rect.midtop = (self.difficultyx + self.offset, self.difficultyy)
                self.state = 'Difficulty'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
        elif self.state == 'Difficulty':
            pass
        elif self.state == 'Word Length':
            pass
            self.game.curr_menu = self.game.word_length_picker
        elif self.state == 'Language':
            # TO-DO: Trigger the game with the selected language
            pass
        elif self.state == 'Theme':
            # TO-DO: Choose which theme
            pass
        self.run_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill (self.game.BACKGROUND)
            self.game.draw_text('Credits', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Authors:', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('- Nadine Obeid -', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('- Edward Tandia -', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('- Arturo Garcia Luna Beltran -', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.blit_screen()

# Not working yet - to fix
class WordLengthMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        if self.game.word_length == 6:
            self.state = 'Six'
        elif self.game.word_length == 5:
            self.state = 'Five'
        elif self.game.word_length == 4:
            self.state = 'Four'
        self.difficultyx, self.difficultyy = self.mid_w, self.mid_h + 30
        self.lengthx, self.lengthy = self.mid_w, self.mid_h + 60
        self.languagex, self.languagey = self.mid_w, self.mid_h + 90
        self.themex, self.themey = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.difficultyx + self.offset, self.difficultyy)  # assign a start position to the cursor

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Four', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Five', 30, self.difficultyx, self.difficultyy)
            self.game.draw_text('Six', 30, self.lengthx, self.lengthy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Four':
                self.cursor_rect.midtop = (self.lengthx + self.offset, self.lengthy)
                self.state = 'Five'
            elif self.state == 'Five':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Six'
            elif self.state == 'Six':
                self.cursor_rect.midtop = (self.themex + self.offset, self.themey)
                self.state = 'Four'
        elif self.game.UP_KEY:
            if self.state == 'Four':
                self.cursor_rect.midtop = (self.themex + self.offset, self.themey)
                self.state = 'Six'
            elif self.state == 'Five':
                self.cursor_rect.midtop = (self.languagex + self.offset, self.languagey)
                self.state = 'Four'
            elif self.state == 'Six':
                self.cursor_rect.midtop = (self.lengthx + self.offset, self.lengthy)
                self.state = 'Five'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
        elif self.state == 'Four':
            self.game.word_length = 4
            self.game.words_pool = words.english_4L
        elif self.state == 'Five':
            self.game.word_length = 5
            self.game.words_pool = words.english_5L
        elif self.state == 'Six':
            self.game.word_length = 6
        self.game.words_pool = words.english_6L
        self.run_display = False






