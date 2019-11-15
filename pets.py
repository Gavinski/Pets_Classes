class Pet:
    totalPets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 88
        Pet.totalPets = Pet.totalPets + 1

    def speak(self):
        print(self.name + " is speaking")

    def feed(self, value=10):
        self.health = self.health + value
        if self.health > 100:
            self.health = 100
            print(self.name + " is full !!")
        else:
            print(self.name + " is still hungry")

    def sit(self):
        print(self.name + " sits")

    def sold(self):
        print(self.name + " got sold")
        Pet.totalPets = Pet.totalPets - 1


class Fish(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        Pet.totalPets = Pet.totalPets + 1

    def speak(self):
        print(self.name + " bubbles")


