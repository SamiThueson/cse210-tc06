class Guess:
    def __init__(self):
        self.guess_list = ['-', '-', '-', '-']

    def get_playerGuess(self, guess_list):
        for n in range(2):
            guess = input('What is your guess? ')
            guess_list.append(guess)
            n + 1
        return guess_list


    def check_guess(self, player_guess):
        check = False
        while not check:
            try:
                player_guess = int(input('What is your guess? '))
                if player_guess >= 1000 and player_guess <= 9999:
                    return player_guess
                    check = True
            except ValueError as ex:
                print(f'{ex} is not a number.')
                player_guess = ''