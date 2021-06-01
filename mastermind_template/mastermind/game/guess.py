class Guess:
    def __init__(self):
        self.player_guess1 = ''
        self.player_guess2 = ''

    def get_playerGuess1():
        player_guess1 = int(input('What is your guess? '))
        return player_guess1

    def get_playerGuess2():
        player_guess2 = int(input('What is your guess? '))
        return player_guess2

    def check_guess(self, player_guess):
        check = True
        while not check:
            if player_guess < 1000:
                print(f'{player_guess} is not in range! Enter a number between 1000 & 9999')
            elif player_guess > 9999:
                print(f'{player_guess} is not in range! Enter a number between 1000 & 9999')
            elif type(player_guess) == str:
                    print(f'{player_guess} is not in range! Enter a number between 1000 & 9999')
            else:
                check = True