#Filter, Map, Reduce - Higher Order Function

import re

'''
Filter - The filter function is used to filter out the elements of an iterable(sequence) depending on a function that tests each element in the sequence to be true or not.
-> it returns those elements of sequence, for which function is ture.
-> it takes 2 arguments (Function,iterable)

Syntax:
filter(function_name,iterable)

Function_name = it's name of a function which tests each element in the sequence return true or false. If function is None, returns the elements that are ture.

Iterable = It is maybe either a squence, list, string, tuple, a container which supports  iteration.

-> it Filters only.
'''

a = [10,40,20,70,30,90,100,60]

def highest_marks(n):
	if n >= 80:
		return True

result = filter(highest_marks,a)
print(result)
print(type(result))

# or

result = list(filter(highest_marks,a1))
print(result)
print(type(result))

# ex-33 | map example
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "AB", fruit)

print(list(map_object))

# or

result = list(filter(lambda n : (n >= 80),a))
print(result)
print(type(result))


'''
Map - This function executes a specified function on each element of the iterable(sequence) and perhaps changes the elements.

syntax:
map(function_name,iterable)

function_name = It's name of a function which perform an operation on all the elements of the sequence and modified elements are returned which can be stored in another sequence.

Iterable = It is maybe either a squence, list, string, tuple, a container which supports  iteration.

-> it can chnage to. 
'''
# ex.1
a = [10,20,30,40,50]

def fun_increment(n):
	return (n + 2)

result = map(fun_increment,a)
print(result)
print(type(result))

# or

result = list(map(fun_increment,a))
print(result)
print(type(result))

# or

result = list(map(lambda n : (n + 2),a))
print(result)
print(type(result))

#or

def remove_punctuation(word):
     return re.sub(r'[!?.:;,"()-]', "", word)

remove_punctuation("...Hello!")


# ex.2
a = [10,20,30,40,50]
b = [5,4,3,2,1]

result = list(map(lambda n,m : n + m,a,b))
print(result)
print(type(result))


'''
reduce - This function is used to reduce a sequence of elements to a single value by processing the accordign to a funtion supplied. It returns a single value.

-> This function is a part of functools module. So first you should import it. 

Syntax:
from functools import reduce
reduce(functon_name, iterable)
'''

from functools import reduce

a = [10,20,30,40,50]

result = reduce(lambda n,m : (n + m),a)
print(result)
print(type(result))
