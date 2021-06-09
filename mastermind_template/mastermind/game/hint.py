import random
class Hint:

    """This checks the number given byt the user and displays the x, o and * characters
     

     Attributes:
     number(integer): The number given by the user
     guess(integer): The number that is going to be guesses by the user
     """

    def __init__(self):
        """The class constructor 
        """
        self.number_list = []
       
        self.symbols = []

    def check_hint(self, guess):
        index = 1
        while index <= len(self.number_list):
            if guess[index - 1 ] not in self.number:
                self.hint[index - 1] = '*'
            elif guess[index - 1] == self.number_list[index - 1]:
                self.hint[index - 1] = 'x'
            elif guess[index - 1] in self.number_list:
                self.hint[index - 1] = 'o'
            
            index += 1

        return self.symbols