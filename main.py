from game4 import Game4
from game6 import Game6
from game import Game

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()