class GameLoop:
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            self.game.update()
            self.game.render()
            self.game.clock.tick(self.game.fps)