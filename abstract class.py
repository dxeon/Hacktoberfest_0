'''
Abstract Class and Abstract Method in Python

-> a class derived from ABC class which belongs to abc module, is known as abstact class in python.

-> abstact class have two methods
1. Abstact Method
2. Concrete Method

-> We can not make an object of an abstract method.
-> we method write method in the child class of abstact class.

Syntax:
from abc import ABC, abstractmethod

class c_name(ABC):

	@abstractmethod
	def meth_name(self): #abstact method
		pass

	def disp(self): #Concrete Method / Method with body
		print('Anything')
'''
# ex.
from abc import ABC, abstractmethod


class father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show1(self):
        print('Concrete method')


class child(father):
    def disp(self):
        print('Child Class')
        print('Defining Abstract Method')


c = child()
c.disp()
c.show()

# EXAMPLE 2
from abc import ABC, abstractmethod


class Defence(ABC):

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print('AK 47')


class Army(Defence):

    def area(self):
        print('Army: LAND')


class AirForce(Defence):
    def area(self):
        print('AirForce: AIR')


class Navy(Defence):
    def area(self):
        print('Navy: Water')


a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print('--------')
af.gun()
af.area()
print('--------')
n.gun()
n.area()
print('--------')
