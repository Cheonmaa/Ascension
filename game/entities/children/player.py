import config

class Player:
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_to_team(self, entity):
        if len(self.team) < config.MAX_TEAM_SIZE:
            self.team.append(entity)
            print(f"{entity} ajouté à l'équipe de {self.name}.")
        else:
            print(f"L'équipe est déjà complète ({config.MAX_TEAM_SIZE} personnages max).")
