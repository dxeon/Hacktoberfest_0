'''
Single Level Inheritance
-> Inheritance is defined as the capability of one class to derive or inherit the properties from some other class and use it whenever needed. Inheritance provides the following properties:
-> It represents real-world relationships well.
-> It provides reusability of code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
-> It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
'''


class A:  # super class, parent classs, Base class
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


class B(A):  # Derived class, childclass
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')


a = A1()
a.feature1()
a.feature2()

b = B()
b.feature3()
b.feature4()

# -----------------------------------------
# inherit

a = B()
a.feature1()
a.feature2()
a.feature3()
a.feature4()


# ---------------------------------------
# Object calling
class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B(A):
    # def __init__(self):
    # 	print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


b = B()

'''
-> IF we want to call both class's init method we use Super() method.
-> It refers to parent class. So we can access all the methods of parent class.
'''


# ex.

class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B(A):
    def __init__(self):
        super().__init__()
        print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


b = B()

'''
-> If we have 2 super class -> that time object use MRO(Method Resolution Order) 
-> It will start from Left to Right.
-> Ex. 2 class.. A and B. So it will take A's init.
'''


# ex.

class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B:
    def __init__(self):
        print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


class C(A, B):
    def __init__(self):
        super().__init__()
        print("__init__ of C")


c = C()


#Multi-Level Inheritance
#Example
 
class grandparent:                 # first lvl 
    def func1:                   
        print(“Hello Grandparent”)
 
class parent(grandparent):         # second lvl
    def func2:                   
        print(“Hello Parent”)
 
class child(parent):               # third lvl
    def func3:                   
        print(“Hello Child”)   
                               
 
# Driver
test = child()                     # object created
test.func1()                       # 3rd lvl calls 1st lvl
test.func2()                       # 3rd lvl calls 2nd lvl
test.func3()                       # 3rd lvl calls 3rd lvl



#Hybrid Inheritance

#Example

 
class parent1:                            # 1st parent class
    def func1:                   
        print(“Hello Parent”)
 
 
class parent2:                            # 2nd parent class
    def func2:                   
        print(“Hello Parent”)
 
class child1(parent1):                    # 1st child class
    def func3:                   
        print(“Hello Child1”)
 
 
class child2(child1, parent2):            # 2nd child class
    def func4:                   
        print(“Hello Child2”)   
                               
 
# Driver Code
test1 = child1()                          # object created
test2 = child2()
 
test1.func1()                       # child1 calling parent1 
test1.func2()                       # child1 calling its own 
 
test2.func1()                       # child2 calling parent1 
test2.func2()                       # child2 calling parent2 
test2.func3()                       # child2 calling child1 
test2.func4()                       # child2 calling its own 


class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  
