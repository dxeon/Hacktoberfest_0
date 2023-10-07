# Types of Methods
# 1. Instace Methods
# 2. Class Methods
# 3. Static Methods


# Instance Method
class student:
	school = "Python University"

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):  #instance method -> works with object
		return (self.m1 + self.m2 + self.m3 )/3

s1 = student(10,20,40)
s2 = student(50,60,70)

print(s1.avg())

'''
Instance method have 2 different types
1. Accessor Method -> only fatch value -> getters
2. Mutator Method -> modify value -> setters 
'''

class student:
	school = "Python University" #class namespace

	def __init__(self,m1,m2,m3):
		self.m1 = m1 #instance namespace
		self.m2 = m2
		self.m3 = m3

	def avg(self):  #instance method -> works with object
		return (self.m1 + self.m2 + self.m3 )/3

	def get_m1(self): #getters
		return self.m1 #get

	def set_m1(self,value): #setters
		self.m1 = value #modification
		return self.m1

s1 = student(60,90,20)
s2 = student(90,90,00)


print(s1.get_m1())
print(s1.set_m1(23))
#just call the functions and it will get and change values accordingly.

'''
Class Method: 

'''
class student:
	school = "Python University" #global

	def __init__(self,m1,m2,m3): #method
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	@classmethod #decorators
	def info(cls): #work with class variable
		return cls.school

	def avg(self):  #instance method -> works with object
		return (self.m1 + self.m2 + self.m3 )/3

s1 = student(10,20,30)
s2 = student(50,60,70)

print(s1.avg())

print(student.info()) #call class method using class name


# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.

'''
Static Method
-> Which not concern with the variables that time we use static method.
-> When use: Operation which does not concern with class object but it is used with other class object that time we use it.
ex. Factorial Number
'''

class student:
	school = "Python University"

	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):  #instance method -> works with object
		return (self.m1 + self.m2 + self.m3 )/3


	@classmethod
	def info(cls):
		return cls.school

	@staticmethod
	def info_static(): #leave argumnet blank
		return "Static method"

s1 = student(10,20,30)
s2 = student(50,60,70)

print(s1.avg())

print(student.info())
print(student.info_static())
