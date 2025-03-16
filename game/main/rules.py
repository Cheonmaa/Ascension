class Rules:
    def __init__(self):
        self.rules = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }

    def get_winner(self, player1, player2):
        if player1 == player2:
            return 'draw'
        if self.rules[player1] == player2:
            return 'player1'
        return 'player2'