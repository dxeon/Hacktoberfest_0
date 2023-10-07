'''
PolyMorphism

Poly -> Many
Morph -> Form
-> 1 thing can take many forms.
-> Ex. we behave differently at diffrent movement.

Ways to impliment polymorphism
1) Duck Typing
2) Operator Overloading
3) Method Overloading
4) Method Overriding
'''

'''
1. Duck Typing
-> Ex. For example, if a bird, walk like a duck, sound like a duck and swim like a duck.. than it is obviously a duck.
'''
class pycharm:
	def execute(self):
		print('Compiling')
		print('Running')

class MyEditor:
	def execute(self):
		print("Spell Check")
		print('Compiling')
		print('Running')
		print('Auto Code')

def myfun(obj):
	obj.execute()

lap1 = pycharm()
myfun(lap1)

'''
2) Method Overloading
-> When more than one method whith same name is defined in the same class, it is known as method overloading.
-> Actully no conecpt like method overloading in python but we can achive it through following program.
'''
# ex.
class Myclass:
	def sum(Self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			s = a + b + c
		elif a!=None and b!=None:
			s = a + b + c
		elif a!=None:
			s = a
		else:
			s = "Atleast provide 3 Values"
		return s

obj = Myclass()
print(obj.sum(1,2,3))

'''
3) Method Overriding
'''
# ex
class add:
	def result(self,a,b):
		print(a+b)

class multi(add):
	def result(self,a,b):
		super().result(a,b)
		print(a*b)

m = multi()
m.result(10,20)


'''
4) Operator Overloading
-> Operator -> +,-,*,/,..
-> in A + B -> A and B are Operands, and + is Operator
'''
# ex for already defined method

a = 5
b = 20

print(a + b)
print(int.__add__(a,b)) #int -> class and __add__ is method #behind the scenes

a = 'python'
b = 'language'

print(a+b)
print(str.__add__(a,b))

#ex
class A:
	def __init__(self,x):
		self.x = x

	def __add__(self,other):
		return self.x + other.x

class B:
	def __init__(self,x):
		self.x = x

a = A(100)
b = B(200)

print(a+b) # behind -> 	A.__add__(self,other)

# ex.2

class student:
	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self,other):
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2
		s3 = student(m1,m2)
		return s3

s1 = student(50,60)
s2 = student(60,70)

s3 = s1 + s2
print(s3.m1)
