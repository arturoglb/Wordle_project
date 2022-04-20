**Authors: Nadine Obeid, Edward Tandia, and Arturo García Luna Beltrán** 

# wordle_game
A game project in python. 

First, we load and explore a dataset containing a useful list of about 370,000 English words published on Github. Second, we discarded any words that are not constructed of exactly 5 characters in length. Next, we found ##### words that we could use for the game. Finally, we randomly choose a set of ###### words that the user will try to guess.

#### We define some set of rules that the game will follow: 
1)
2)
3)
4)
5)
6) 

#### Possible extensions: 
1)
2)
3)
4)
5)
6)

## Code
Describe each of the files that we will work on.
* **parameters.py** contains the parameters, including saving and data path, and model's hyper-parameters and constant. The parameters also define the unique name under which the analysis result will be saved.
* **data.py** organize the data loading and data-pre-processing
* **map.py** 
* **data_exploration**  

## Run order
1) *data_exploration.py*
2) *train_models.py*
3) *test_performances.py*

## Data
The data could be downloaded on:https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt

Once the data is downloaded and uncompressed, one should either set it in a folder "data" or update the default path in: parameters.DataParams.dir = 'data/' to the data location.