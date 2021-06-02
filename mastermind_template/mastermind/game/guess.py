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
        check = False
        while check == False:
            try:
                player_guess = int(input('What is your guess? '))
                if player_guess >= 1000 and player_guess <= 9999:
                    check = True
                    return player_guess
                else:
                    print(f'{player_guess} is not in range')
            except ValueError as ex:
                print(f'{ex} is not a number.')