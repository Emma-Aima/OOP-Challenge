# The output of the Pet class (Rabbit)
# The name of the pet rabbit is Tommy

class Pet:
	def __init__(self, name):
		self.name = name
		self.hunger = 5
		self.energy = 5
		self.happiness = 5
		self.tricks = []

	def eat(self):
		self.hunger = max(0, self.hunger - 1)
		print(f"{self.name} is eating...")

    # Think about edge cases like trying to play when energy is 0.
	def play(self):
		if self.energy > 0:
			self.happiness = min(10, self.happiness + 1)
			self.energy -= 1
			print(f"{self.name} is playing...")
		else:
			print(f"{self.name} is too tired to play.")

	def sleep(self):
		self.energy = min(10, self.energy + 2)
		print(f"{self.name} is sleeping...")

# Creating pet: Tommy
Tommy = Pet("Tommy")
Tommy.eat()
Tommy.play()
Tommy.sleep()

print(f"{Tommy.name}'s current status:")
print(f"Hunger: {Tommy.hunger}")
print(f"Energy: {Tommy.energy}")
print(f"Happiness: {Tommy.happiness}")

Tommy.tricks = ['fetch', 'stand on hind legs']
print(f"Tricks: {Tommy.tricks}")


# Think about edge cases like trying to play when energy is 0.
def play(self):
	if self.energy < 0:
		self.happiness = min(10, self.happiness - 1)
		self.energy += 1
		print(f"{self.name} is feeling too tired to play.")