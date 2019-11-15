import pets


class Dog(pets.Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.good_boy = True

    def speak(self):
        if self.good_boy:
            print(self.name + " says: Bark")
        else:
            print(self.name + " says: we should over through the government")

    def sit(self):
        if self.good_boy:
            print(self.name + " is a goodboy and sits")
        else:
            print(self.name + " is a bad boy and doesnt sit")


class Cat(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.good_boy = False