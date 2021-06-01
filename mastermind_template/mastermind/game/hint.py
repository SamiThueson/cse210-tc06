import random
class Hint:

    """This checks the number given byt the user and displays the x, o and * characters
     

     Attributes:
     number(integer): The number given by the user
     guess(integer): The number that is going to be guesses by the user
     """

    def __init__(self,number,guess):
        """The class constructor 
        """
        self.number = number
        self.guess = random.randint[1000,9999]


    def display_hint(self):
        guess_list = list(self.guess)
        number_list = list(self.number)

        idx = 0
        for x in number_list:
            if x in guess_list and x not in guess_list[idx]:
                print("o",end="")
            elif x ==guess_list[idx]:
                print("x",end="")
            else:
                print("*",end="")

            idx += 1



