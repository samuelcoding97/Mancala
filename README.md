# Mancala.py
###About
This program allows the user to play a text-based version of Mancala using a Python class with functions. You can read about the history of the game on <a href="https://en.wikipedia.org/wiki/Mancala">Wikipedia</a> and the rules on this <a href="https://endlessgames.com/wp-content/uploads/Mancala_Instructions.pdf">website</a>. This is the final project for Intro to Programming II at Oregon State. The program uses a 14 integer list to create the board, with the first 6 integers being the cups for player 1, the 7th integer being player 1's store, the 8th - 13th integers being player 2's cups, and the 14th integer being player 2's store.

The list before gameplay looks like this, with 4 seeds in each cup and 0 in each store:

Photo

It can be visualized on a mancala board like this:

Photo

####Initializing the class
The Mancala class item is initialized without any input. This item allows the user to call functions for normal gameplay.

PHOTO

For example: a class item could be created with game = Mancala()

#### Creating players
The function create_player assigns names to Player 1 and Player 2. 

PHOTO

For example: a player could be created with game.create_player("Sam")

#### Viewing the board
the function print_board() takes no parameters and returns the location of each of the seeds on the board, as well as the number of seeds in the store of each player

PHOTO

PHOTO
an example of print_board() midway through the game

#### Finding the winner
The function return_winner() takes no parameters, and checks to see if the game has finished. Uses an iterative conditional to find if one of the players has zero seeds in all of their cups, since this indicates the end of the game. If both players still have seeds in their cups, the function will return "Game has not ended". If the game has ended, the function compares the total of each player's store. It returns "Winner is player 1", "Winner is player 2" or "It's a tie" depending on the outcome.

#### Taking turns
By far the most complex function of the program is play_game() which takes as input a 1 or 2 to indicate the player, and an index from 1-6 to indicate the cup to draw from. 

Before making a move, the function checks to see if the index is out of range and also calls return_winner() to check if the game has ended.

PHOTO

The index is decremented or increased to match the index values of the respective player's cups (Player 1: index -= 1, Player 2: Index += 6). The seed count is gathered from that cup, and with an iterative process a seed is placed in each subsequent cup and store, unless it is the other player's store, in which case that index is skipped. There is a conditional process to check if the last seed results in a <a href="https://mancala.fandom.com/wiki/Capturing_(game_mechanism)">seed steal</a>. There is also a conditional process to check if the last seed lands in the player's store, which results in another turn.

PHOTO

After the player has taken their turn, there is a check to see if either of the players now has 0 seeds in all of their cups. If for example, Player 1 has 0 seeds, then Player 2 immediately puts all of their seeds into their own store. The program will recognize the game has ended the next time return_winner() or play_game() is executed.

PHOTO
