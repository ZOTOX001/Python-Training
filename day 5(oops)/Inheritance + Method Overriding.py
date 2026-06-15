class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal):

    def sound(self):
        print("Bark")


d1 = Dog()

d1.eat()
d1.sleep()
d1.sound()