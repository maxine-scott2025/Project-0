class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False
        self.inventory = []
    
    def talk_to_player(self, player_name,):
        if self.received == False:
        print(f"{self.name} says: '{Hi {player_name}. Im looking for a star. Do you have one for me?}'")
        YN = input("Do you have a star? (y/n): ")
        if YN == "y":
            print(f"{self.name} says: 'Thank you! I will give you a star in return.'")
            
        else:
            print(f"{self.name} says: 'I need a star to continue my journey. Please help me.'")

    def receive_star(self, item):
        self.received = True
        self.append(item)
        print(f"{self.name} says: 'Thank you for the {item.name}! Here is your reward.'")
