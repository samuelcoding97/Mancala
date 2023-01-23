# Author: Samuel Miller
# GitHub username: samuelcoding97
# Date: November, 21 2022
# Description: This is the portfolio project. It creates a class named Mancala which allows the user
# to call functions and effectively play the game.

class Mancala:
    """
    initializes a mancala object with players set to none, the board set to the standard 4 seeds per
    cup and special list slices for each player's store and seeds
    """
    def __init__(self):
        self._player1 = None
        self._player2 = None
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def create_player(self, name):
        """
        initializes the player value. name to be inputted as a string.
        """
        # if there is not a player1, initialize name to player 1
        if self._player1 is None:
            self._player1 = name

        # otherwise initialize it to player2
        else:
            self._player2 = name

    def print_board(self):
        """
        takes no parameters and returns the board status. shows the store of each player
        and the seeds they have as well
        """
        print("player1:")
        # str allows both data types to be concatenated
        print("store: " + str(self._board[6]))
        print(self._board[0:6])
        print("player2:")
        print("store: " + str(self._board[13]))
        print(self._board[7:13])
        return

    def return_winner(self):
        """
        takes no parameters. Checks to see if the game is over. If it is returns the winner,
        or the existence of a tie. If the game is not over, returns game has not ended
        """
        player1_total = 0
        player2_total = 0
        for element in range(len(self._board[0:6])):
            player1_total += (self._board[0:6])[element]
        for element in range(len(self._board[7:13])):
            player2_total += (self._board[7:13])[element]
        if player2_total != 0 and player1_total != 0:
            return "Game has not ended"
        elif player1_total == 0:
            self._board[13] += player2_total
        elif player2_total == 0:
            self._board[6] += player1_total
        # if all seed cups are equal to 0, and player 1's store has more seeds, she wins
        if self._board[6] > self._board[13]:
            return "Winner is player 1: " + self._player1
        # if all seed cups are equal to 0, and player 2's store has more seeds, she wins
        elif self._board[13] > self._board[6]:
            return "Winner is player 2: " + self._player2
        # if all seed cups are equal to 0, and the stores are equal in count, it's a tie
        else:
            return "It's a tie"

    def play_game(self, player, index):
        """
        takes a player, either 1 or 2, and an index from 1-6. Player parameter dictates
        whose turn it is, index parameter dictates which seed cup is being played.
        returns the board to the user. If the last seed lands in a players store, prints
        a statement telling that player to go again.
        """
        # testing for index range
        if index > 6 or index <= 0:
            return "Invalid number for pit index"
        # calls return_winner to check if the game has ended
        if self.return_winner() != "Game has not ended":
            return "Game is ended"

        if player == 1:
            # in order to match the python index starting at 0
            index -= 1
            seed_count = self._board[index]
            # take all the seeds out of the specified cup
            self._board[index] = 0
            # place one seed in each cup following the selected cup
            for seed in range(seed_count):
                index += 1
                # if the indicated cup is the other players store, skip that
                # and go to the beginning
                if index == 13:
                    index = 0

                # special case for stealing seeds, if it's the last seed and the cup it is entering
                # is empty, it takes that seed and any in the opponents corresponding cup and places
                # in their own store
                if seed == (seed_count - 1) and self._board[index] == 0 and 0 <= index <= 5:
                    # the cup being stolen from
                    seed_steal = self._board[-(index + 2)] + 1
                    # remove the seeds from the board and place them in the store
                    self._board[-(index + 2)] = 0
                    self._board[6] += seed_steal
                    break

                self._board[index] += 1
                # special case for the last seed landing in player's store
                if seed == (seed_count - 1) and index == 6:
                    print("player 1 take another turn")

        if player == 2:
            index += 6
            seed_count = self._board[index]
            self._board[index] = 0
            for seed in range(seed_count):
                index += 1
                # if index is 14, we have left the list and need to return to the beginning
                if index == 14:
                    index = 0
                # if the indicated cup is the other players store, skip that
                # and go to the next
                elif index == 6:
                    index = 7

                # special case for stealing seeds, if it's the last seed and the cup it is entering
                # is empty, it takes that seed and any in the opponents corresponding cup and places
                # in their own store
                if seed == (seed_count - 1) and self._board[index] == 0 and 7 <= index <= 12:
                    # the cup being stolen from
                    seed_steal = self._board[(12 - index)] + 1
                    # remove the seeds from the board and place them in the store
                    self._board[(12 - index)] = 0
                    self._board[13] += seed_steal
                    break

                self._board[index] += 1
                # special case for the last seed landing in player's store

                if seed == (seed_count - 1) and index == 13:
                    print("player 2 take another turn")

        player1_total = 0
        player2_total = 0
        for element in range(len(self._board[0:6])):
            player1_total += (self._board[0:6])[element]
        for element in range(len(self._board[7:13])):
            player2_total += (self._board[7:13])[element]
        if player1_total == 0:
            self._board[13] += player2_total
            for element in range(len(self._board[7:13])):
                self._board[element + 7] = 0
        elif player2_total == 0:
            self._board[6] += player1_total
            for element in range(len(self._board[0:6])):
                self._board[element] = 0
        return self._board

game = Mancala()
player1 = game.create_player("Lily")
player2 = game.create_player("Lucy")
print(game.play_game(1, 3))
game.play_game(1, 1)
game.play_game(2, 3)
game.play_game(2, 4)
game.play_game(1, 2)
game.play_game(2, 2)
game.play_game(1, 1)
game.print_board()
print(game.return_winner())