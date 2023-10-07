'''
Python Supports
-> OOP - Class
-> POP - Small Functions(modules)

Q. What is Object?
-> We solve real world issue with virtal world programming. In the real world everything is object. Ex. If the one wants to record something, he require a camera, In every company every employee is an object and they use laptop object. Every object has some attributes(properties,behaviour)
ex. Properties - Name, Height, Skin color, ..
Behaviour(Action) - Talking, Walking, ..

-> If we want to store something in object we need to define variables
-> If you want to define the behavior we need to use methods

----------------------------------------------------------------------------------------
OOPS TOPICS:

Class - design of the object (Bluprint)
Object - instance of class
Method
Inheritance
Polymorphism
Data Abstraction
Encapsulation

Method : The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.

Inheritance: Inheritance is the most important aspect of object-oriented programming, which simulates the real-world concept of inheritance. It specifies that the child object acquires all the properties and behaviors of the parent object.By using inheritance, we can create a class which uses all the properties and behavior of another class. The new class is known as a derived class or child class, and the one whose properties are acquired is known as a base class or parent class.It provides the re-usability of the code.

Polymorphism : Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape. By polymorphism, we understand that one task can be performed in different ways. For example - you have a class animal, and all animals speak. But they speak differently. Here, the "speak" behavior is polymorphic in a sense and depends on the animal. So, the abstract "animal" concept does not actually "speak", but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

Encapsulation: Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because data abstraction is achieved through encapsulation.

Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.
----------------------------------------------------------------------------------------

Class: Class is a group of attributes and methods
Attribute - variable which contains data
Method(Behaviour) - it performs an action or task (similar to function)

class laptop:
    def Configuration(self):
        print("i5 7th gen 1tb SSD")

computer1 = laptop()
computer2 = laptop()
computer3 = laptop()

# print(type(computer1))
laptop.Configuration(computer1)
laptop.Configuration(computer2)

computer1.Configuration()
computer2.Configuration()
computer3.Configuration()

syntax:
class Classname(object): #object is optional
	# attributes and methods
	def __init__(self):
        #constructor -> use to initialize variables
        # it will call automatically
        self.variable_name = value #attributes
        self.variable_name = 'value' #attributes

    def method_name(self): #constructor
        # ..code..

    #self is variable

Class - key word to create class and it's name generally start from Capital letter
ex. class Myclass:
        def __init__(self):
            self.model = 'harsh'

        def show_model(self):
            print('Model',self.model)

object - object represents the base class name from where all classes in Python are derived.
This class is also derived from object class. This is optional

__init__ - This method is used to initialize the variables. This is a special method. We do not call this method explicitly.

self - it refers to current class instance/object
'''


class laptop:
    def Configuration(self2):
        print("i9 7th gen 1tb SSD")


computer1 = laptop()
computer2 = laptop()

# print(type(computer2))
laptop.Configuration(computer1)
laptop.Configuration(computer2)

# or

computer1.Configuration()
computer2.Configuration()


# -------------------------------------------------------------------------

# INIT Method

# ex.1
class laptop:
    def __init__(self):  # It runs how many times object called
        print('THIS IS __init__')

    def Configuration(self):
        print("i5 7th gen 1tb SSD")


computer1 = laptop()
computer2 = laptop()

computer1.Configuration()
computer2.Configuration()


# ex.2
class laptop:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def Configuration(self):
        print('Configuration is:', self.cpu, self.ram)


computer1 = laptop('i5 7th gen', 36)
computer2 = laptop('i5 11th gen', 68)
# in background we pass 3 arguments - computer1,cpu,ram

computer1.Configuration()
computer2.Configuration()


# -------------------------------------------------------------------------

class computer:
    pass


c1 = computer()
c2 = computer()
print('Address: \nc1:', id(c1), '\nc2:', id(c2))


# -> When we create object, it automatically call __init__ method.

class computer:
    def __init__(self):
        self.name = 'Harsh'
        self.age = 10


c1 = computer()
c2 = computer()

print(c1.name)
print(c2.name)

# -> in this, if we want to assign our perosnal value:

c1.name = "JAVA"
c2.age = 20

print(c1.name)
print(c2.age)


# -------------------------------------------------------------------------
# WHY SELF:
# ex.

class Computer:
    def __init__(self):
        self.name = 'Harsh'
        self.age = 20

    def update(self):  # self will ensure that which object I'm talking about
        # is that c1 or c2. so from c1.update() we can distinguish that.
        self.age = 25


c1 = Computer()
c2 = Computer()

c1.update()

print('C1:', c1.age)


# also we can compare it through attribute
# ex.

class Computer:
    def __init__(self):
        self.name = 'Harsh'
        self.age = 20

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()

# c1 = 30
# c2 = 20
if c1.compare(c2):
    print('Both are same')
else:
    print('Not Same')


# -------------------------------------------------------------------------

class Computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer("Harsh", 45)
c2 = Computer("Python", 30)

if c1.compare(c2):
    print('Both are same')
else:
    print('Not Same')
