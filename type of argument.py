'''
2 Arguments
1. Actual
2. Formal

-> Types of Actual Arguments in Function:
1. Positional Argument
2. Keyword Argument
3. Default Argument
4. Variable Length Argument
5. Keyworded variable Length Argument
'''

# 1. Positional Argument
# -> correct positional order
# -> Number should be same for Actucal and formal

# ex.
def show(x,y):
	z = x ** y

# 2. Keyword Argument
# -> The arguments are passed to the function with name-value pair so keyword arguments can identify the formal argument by their name.

# ex.
def show(name,age):
	print(name,age)

show(age=25,name="Python")

# -> argument number should be maintain
# -> order does not


# 3. Default Argument
# -> We already provide default value at funciton defineition.

# ex.
def show(name,age=20):
	print(name,age)

show('Python')

# 4. Variable Length Argument
# -> Variable Length Argument is an argument that can accept any number of values. The variable length is written with * symbol.
# -> stores values in tuple.

# ex.
def add(*num):
	a = num[0] + num[1] + num[2]
	print(a)

add(5,6,2)

# ex.2
def add(x,*num):
	a = x + num[0] + num[1]
	print(a)

add(5,6,2) # x = 5 and num = 6,2

# 5. Keyworded Variable Length Argument
# ex.1
def person(name,**data):
	print(name)
	print(age)

person('Harsh',age=10,city='Ahmedabad',mob=1365831813)

# ex.2
def person(name,**data):
	print(name)
	for i,j in data.items():
		print(i,':',j)

person('Harsh',age=10,city='Ahmedabad',mob=1365831813)
