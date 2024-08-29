class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.received = False

    def pickup(self):
        ask = input(f"Do you want to pick up the {self.name}? (y/n): ")
        if ask == "y":
        self.received = True
            print("You picked up the {self.name}! {self.description}")
        else:
        print("You left the {self.name} behind. Would you still like to know what {self.name} is? (y/n): ")
        if ask == "y":
                print(f"{self.description}")
