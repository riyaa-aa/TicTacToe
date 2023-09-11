import math
import random

class Player:
    def __init__(self, letter): # letter is either x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player): # inheritance
    def __init__(self, letter):
        super().__init__(letter)
        self.letter = letter
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        # picking a random empty spot on the board
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8). ' )
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
