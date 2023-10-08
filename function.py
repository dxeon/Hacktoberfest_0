'''-----------------------------------------------
syntax
function definition
def function_name(parameters):
	...code...
	...code...
	...code...
function call()
function_name(parameters)
-----------------------------------------------'''
def fun1(): #define
	print("My Name is harshil")
	c = 13 + 6
	print(c)

fun1() #call


#return
def fun_return():
	return "My Name is keyur"

a = "My Name is Meet savani"
print(a)
print(a)

# Python follows DRY Priniciple  (Don't Repeat Yourself)
def op(x):
	x =  x +  5
	return x

# def fun3(10,20)
# def fun3(x)
# def fun3(x,y)

	


print(op(5)) #call 10
print(op(10)) #15

#pass two valuse
def addition(x,y,z):
	return(x+y+z)

print("Addition:",addition(10,20,30))

#return 2 values
# def one_para(10,20):
#     c = x + y #30
#     d = x * y #200
#     return c,d

a = int(input("Enter your value of A: "))#user
b = int(input("Enter your value of B: "))#user

var1,var2 = 30,200 #c , d
print('addition: ',var1)
print('multiplication: ',var2)

#default argument
def defargu(x=20,y=30):
	return(x+y)

print(defargu(20))
print(defargu())

#function return another function
def display(sh):
	print('DISPLAY FUNCTION')

def show():
	return "SHOW FUNCTION"

return_show = display(show)
print(return_show())

#program
def week_days(day):
	week = day // 7
	days = day % 7
	print('no. of week is {} and days are {}'.format(week,days))
days = int(input('Enter no. of days: '))
week_days(days)


def factorial(n):
	sum = 1
	for i in range(n):
		sum = sum * i
		return sum
print(factorial(5))
