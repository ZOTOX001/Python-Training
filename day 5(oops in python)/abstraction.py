# abstraction doesnt exist  in python we have to import a library for the same from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class abstract_class(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class rectangle(abstract_class):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth    
object = rectangle(5, 10)
object.perimeter()
print(object.perimeter())    
    
#inherting the abstract class than all abstractmethods in abstact class must be implemented
#  in the child class otherwise it will throw an error

