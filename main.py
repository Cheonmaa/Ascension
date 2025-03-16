class Main:
    def __init__(self):
        pass

    def run(self):
        from game.entities.children.Player import Player # type: ignore
        from game.entities.children.Enemy import Enemy # type: ignore
        from game.battle.battle import Battle

        player = Player("Player")
        enemy = Enemy("Enemy")

        battle = Battle(player, enemy)
        battle.start()

if __name__ == "__main__":
    main = Main()
    main.run()