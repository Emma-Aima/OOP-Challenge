# Defining a class called 'Pet'
class Pet:

    def __init__(self, name="Tommy"):
        self.__pet = 1 # Private attribute
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good rest. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had energy to play and is happy! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play and have fun. Let them rest!")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {'Stand on hind legs'.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
    
    def get_status(self):
        print(f"Fetch {self.name}'s Current Status Stand on hind legs")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
    

    # This is how the class can be used for the Pet
    if __name__ == "__main__":
        my_pet = Pet() # The Pet is a rabbit
    
        my_pet.get_status()
        my_pet.eat()
        my_pet.sleep()
        my_pet.play() 
        my_pet.train("Fetch")
        my_pet.show_tricks("Stand on hind legs")
    
    # The rabbit (Tommy) tries to play when energy is 0
     
