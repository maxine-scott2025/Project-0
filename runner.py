from player_Character import player_character
from game_character import game_character
from item import Item
from wordle import playGame

# create a game play senario
def gameplay(player_character, game_character, item):
    print("Welcome to Eldslunds, The Calm Woodlands")
    # create a variable that holds the player character
    Player_name = input("What would you like to name your character? ")
    Player = player_character(Player_name, 100)
    Character = game_character("Elf", ["Hello, how are you?", "I'm doing well, thank you for asking.", "Goodbye!", "My name is {self.name}.", "You have to travel to {item.location} to find {item.name}.", "You have to travel to {item.pathway} to find {item.name}."])
    posion = Item("Posion","Use this when you need to ")
    # create a variable that holds the correct word for the wordle game
    word = 'Elves'
    # Using the the correct word, create a game story that uses the player_character and game_character objects to tell a story that the player can interact with
    print("You are in a forest")
