class Player:
    """A person taking part in a game. The responsibility of Player is to get the 
    players names.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self.name_list = []
    
    def get_name(self, name_list):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            name_list.append(name)
        
        return self.name_list