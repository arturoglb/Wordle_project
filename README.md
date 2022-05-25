**Authors: Nadine Obeid, Edward Tandia, and Arturo García Luna Beltrán** 

# wordle game with add-ons
A game project in python. 

#### We define a set of functionalities that the game will follow: 
1) As this game is a recreation of the wordle game, we established the basic rules that this game considers.
2) We thought of adding some improvements to the game, to make it more attractive to people who do not speak the language used in the game. Therefore, we added 2 more languages "Spanish" and  "French", so more people can enjoy of this wonderful game.
3) We enable different lenght for words, to add a wide variety of words in order to keep the user entertained.
4) In addition, we have added 3 levels of difficulty, where each level will reduce the number of guesses for the player.
6) To make the user experience of the game more attractive, we generated animations and some themes the user can select.

#### Possible extensions: 
1) Implement a time tracking of playtime, this will enable the player to know how long it took him/her to guess the correct word 
2) Share results on social media, so 
3) Implement a two players game for competitions with friends and family 
4) After a word is guess, show the definition of the word for learning purposes
5) Creation of word levels, so the player have a motive to keep playing

## Code
* **main.py** contains the executable of the game, the window of the game will pop up at the moment of running the file.
* **game.py** incorporates all the relevant functions to draw the board, the letters, to check the events, and the most important the game loop.
* **menu.py** creates and organize the menus for the game with classes for each option.
* **words.py** organize the data loading from the csv files containing the words and prepares each list of words for the game.
* **animations.py** contemplates the functions required to generate the flame animation. 
* **Themes.py** organize the images loading and prepares them for the backgrounds of the game.

## Run order
1) *main.py* The only file consider for running is the main file, the different files are linked through it. 

## Data
The words data is allocated on the same folder as the other code files. While running the main file, the various files will consider these data csv files. There is no need to download from an external source.
