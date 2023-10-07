'''
Class inside class
-> we define one class inside another class
-> Make object of inner class in inside outer class
'''

class student:

	def __init__(self,name,roll): #outer class
		self.name = name
		self.roll = roll
		self.lap = self.laptop() #object of inner class

	def show(self):
		print(self.name,self.roll)
		self.lap.show()

	class laptop: #inner class
		def __init__(self):
			self.brand = 'Lenovo1'
			self.cpu = 'i5 7th gen'
			self.ram = 16

		def show(self):
			print(self.brand,self.cpu,self.ram)

s1 = student('Harsh',25)
s2 = student('Python',22)

s1.show()

print(s1.lap.cpu)

# lap1 = student.laptop() #object making outside class

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

#ex-2
class Hello:

	# constructor method


def __init__(self):


# object attributes
self.course = "Campus preparation"
self.duration = "2 months"

# define a show method
# for printing the content


def show(self):


print("Course:", self.course)
print("Duration:", self.duration)

# class object
outer = Hello()

# method calling
outer.show()
