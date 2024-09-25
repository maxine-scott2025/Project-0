class player_Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False
        self.inventory = []
    
    diologue_chart = {
        "hello": "Hello, how are you?",
        "how are you": "I'm doing well, thank you for asking.",
        "goodbye": "Goodbye!",
        "what's your name": "My name is {self.name}.",
        "I'm looking for {item.name}": "You have to travel to {item.location} to find {item.name}.",
        "How do I get to {item.location}": "You have to travel to {item.pathway} to find {item.name}.",
    }
    def pickup(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}.")

    def drop(self, item):
        self.inventory.remove(item)
        print(f"{self.name} dropped {item.name}.")
    
    def talk(self, game_character):
        ask = input(f"Do you want to talk to {game_character.name}? (y/n): ")
        if ask == "y":
            print(f"{self.name} says: Hello, {game_character.name}!")
        