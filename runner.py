from player_Character import PlayerCharacter
from game_character import GameCharacter
from item import Item
from wordle import playGame

# create a gameplay scenario
def gameplay():
    print("Welcome to Eldslunds, The Calm Woodlands")
    
    # Create a variable that holds the player character
    player_name = input("What would you like to name your character? ")
    player = PlayerCharacter(player_name, 100)
    character = GameCharacter("Elf", ["Hello, how are you?", "I'm doing well, thank you for asking.", "Goodbye!", "My name is {name}.", "You have to travel to {item.location} to find {item.name}.", "You have to travel to {item.pathway} to find {item.name}."])
    
    # Create an item
    potion = Item("Potion", "Use this when you need to heal yourself.", "Heal for 20 health points.", "Potion Shop", "Take the path to the east.")
    
    # Create a variable that holds the correct word for the Wordle game
    correct_word = "MAGIC"
    result = playGame(correct_word)

    # Determine the outcome of the Wordle challenge
    if result:  # Assuming playGame returns True if the player wins
        print("You've proven your wit! The Elf gives you a magical potion as a reward.")
        player.pickup(potion)  # Add the potion to the player's inventory
    else:
        print("The Elf shakes his head. 'You must find the right word to proceed.'")

    # Using the correct word, create a game story that uses the player_character and game_character objects to tell a story
    print("You are in a forest. What would you like to do?")
    action = input("Choose: 'explore' or 'talk': ").lower()
    
    if action == "explore":
        print("You venture deeper into the forest, discovering hidden paths and ancient trees.")
        # You can add more interactive elements here
    elif action == "talk":
        character.talk(player)
    else:
        print("Invalid action. The forest remains quiet.")

# To start the gameplay
if __name__ == "__main__":
    gameplay()
