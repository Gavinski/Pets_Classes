from pets import *
from dog import *

print("\nWelcome to my pet shop:")
dog = Dog("Fido", 12)
cat = Cat("Whiskers", 2)
fish = Fish("Goldie", 1)

dog.speak()
dog.sit()
dog.feed(20)
print("\n")
cat.speak()
cat.sit()
cat.feed(10)
print("\n")
fish.speak()
fish.health = 20
fish.sit()
fish.feed(10)

print("\n")
print("Current number of pets: " + str(Pet.totalPets))

fish.sold()

print("Current number of pets: " + str(Pet.totalPets))


