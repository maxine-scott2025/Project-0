class game_character:
    def __init__(self, name, spoken_lines):
        self.name = name
        self.spoken_lines = spoken_lines
        self.inventory = []

    diologue_chart = {
        "hello": "Hello, how are you?",
        "how are you": "I'm doing well, thank you for asking.",
        "goodbye": "Goodbye!",
        "what's your name": "My name is {self.name}.",
        "I'm looking for {item.name}": "You have to travel to {item.location} to find {item.name}.",
        "How do I get to {item.location}": "You have to travel to {item.pathway} to find {item.name}.",
    }
    # write a function that tells the game character what to say using the diologue_chart dictionary
    def talk(self, player_character):
        if ask == diologue_chart[ask]:
            print(diologue_chart[ask])
        
