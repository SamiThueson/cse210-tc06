from game.guess import Guess
from game.hint import Hint
from game.number import Number
from game.player import Player
from game.turn import Turn
import random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.number = Number()
        self.guess = Guess()
        self.turn = Turn()
        self.player = Player('')
        self.name_list = []
        self.guess_list = ['-', '-', '-', '-']
        self.hint = Hint()
        self.symbols = []
        self.keep_playing = True
        self.keep_names = []
        self.player_guesses = []
        self.get_playerGuess = ''

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.player.get_name(self.name_list)
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates(self.player_guesses)

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        
        self.guess.get_playerGuess(self.guess_list)

    def do_updates(self, player_guesses):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.hint.check_hint(self.guess_list)

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        self.guess_list = self.player_guesses
        print(f'Player {self.name_list[0]}: {self.guess_list}, {self.hint.symbols}')
        print(f'Player {self.name_list[1]}: {self.guess_list}, {self.hint.symbols}')