class GameCharacter:
    def __init__(self, name, spoken_lines):
        self.name = name
        self.spoken_lines = spoken_lines
        self.inventory = []

    dialogue_chart = {
        "hello": "Hello, how are you?",
        "how are you": "I'm doing well, thank you for asking.",
        "goodbye": "Goodbye!",
        "what's your name": "My name is {name}.",
        "I'm looking for {item_name}": "You have to travel to {item_location} to find {item_name}.",
        "How do I get to {item_location}": "You have to travel to {item_pathway} to find {item_name}.",
    }

    def talk(self, player_character):
        ask = input("What do you want to say? ").lower()
        if ask in self.dialogue_chart:
            response = self.dialogue_chart[ask].format(name=self.name, 
                                                        item_name="an item",  # Placeholder
                                                        item_location="somewhere",  # Placeholder
                                                        item_pathway="a path")  # Placeholder
            print(response)
        else:
            print("I don't understand that.")