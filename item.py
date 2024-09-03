class Item:
    def __init__(self, name, description, use_description, location, pathway):
        self.name = name
        self.description = description
        self.use_description = use_description
        self.location = location
        self.pathway = pathway
        self.received = False

    def pickup(self):
        ask = input(f"Do you want to pick up the {self.name}? (y/n): ")
        if ask == "y":
        self.received = True
            print("You picked up the {self.name}! {self.description}")
        ask = input(f"Do you want to add {self.name} to your inventory? (y/n): ")
        if ask == "y":
            inventory.append(self)
            print(f"{self.name} has been added to your inventory.")
        else:
            print(f"{self.name} has not been put down.")
        else:
        print("You left the {self.name} behind. Would you still like to know what {self.name} is? (y/n): ")
        if ask == "y":
                print(f"{self.description}")

    def drop(self):
        print(f"{self.item} is in your inventory.")
        ask = input(f"Do you want to drop the {self.item}? (y/n): ")
        if ask == "y":
            print(f"{self.item} has been put down.")
            ask = input(f"Do you want to put it back in your inventory (i)? (y/n): ")
            if ask == "y":
                print(f"{self.item} has been put back in your inventory.")
            else:
                print(f"{self.item} has been put down.")

    def use(self): 
        print(f"{self.item} is in your inventory.")
        ask = input(f"Do you want to use the {self.item}? (y/n): ")
        if ask == "y":
            print(f"You can use {self.item} by {self.use_description}.")
        else:
            ask = input(f"Do you want to drop (d) {self.item} or put it back in your inventory (i)? (d/i): ")
            if ask == "d":
                print(f"{self.item} has been put dropped.")
                ask == "i":
                print(f"{self.item} has been put back in your inventory.")