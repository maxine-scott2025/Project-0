class PlayerCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def pickup(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}.")

    def drop(self, item):
        self.inventory.remove(item)
        print(f"{self.name} dropped {item.name}.")

    def talk(self, game_character):
        ask = input(f"Do you want to talk to {game_character.name}? (y/n): ")
        if ask == "y":
            game_character.talk(self)