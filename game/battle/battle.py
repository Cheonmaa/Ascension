class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"Battle between {self.player.name} and {self.enemy.name} started!")

        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)

        if self.player.is_alive():
            print(f"{self.player.name} won!")
        else:
            print(f"{self.enemy.name} won!")