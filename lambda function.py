'''
Anonymous Function or Lambda Function

Anonymous Function - Function without a name is called as Anonymous Function or Lambda Function.
-> it is not defined using def keyword rather they are defined using lambda keyword.

Syntax:-
lambda argument_list : expression

ex.
lambda x : print(x) #x -> argument(parameter)
lambda x,y : x + y

Calling Lambda Function:
-> it returns function and assign into one variable and can use it later.
ex.
sum = lambda x : x + 1
sum(5)

add = lambda x,y : x + y
add(5,10)

-> it contains only one argument which must be arguments. It can not include statements in 	its body. ex. no use of if,for,..
ex. only x + y
-> No need to write return function
'''

#type 1
def show(x):
	print(x)

show(5)

#type 2
show = lambda x : print(x)

#example
from functools import reduce 

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans) 
show(10)

#passing 2 parameters
add = lambda x,y : x + y
print(add(5,3))

#return 2 values
add = lambda x,y : (x + y , x - y)
# print(add(5,3)) #right ans
a , b = add(5,6)
print(a)
print(b)

#default argument
add = lambda x=2,y=5 : x + y
print(add(5))
