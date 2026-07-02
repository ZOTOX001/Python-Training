# Same method name but different behavior.
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()