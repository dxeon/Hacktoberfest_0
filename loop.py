'''-----------------------------------------------
Python has two primitive loop commands:
  1.while loops
  2.for loops
-----------------------------------------------'''


'''-----------------------------------------------

Loop control - Loop control statements are used when a section of code may either be executed a fixed number of times, or while some condition is true

While - The while loop keeps repeating an action until an associated condition returns false

Syntex :-

variable declaration
while condition:
	...code...

<
>
<=
>=
==
!=
-----------------------------------------------'''

i = 5
while 11 <= 10:
    print(1, "Hiiy")
    i += 2

print("-----------------")


# Continue Keyword
# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#         continue
#     print(i)



# Else statement - This repeatedly tests the condition and, if it is True, executes the Statement 1; if the condition is False (which may be the first time it is tested) the Statement 2 of the else clause, is executed and the loop terminates. The else suite will be always executed irrespective of the statements in the loop are executed or not

i = 2
while i < 10:
    print(i, "Hello")
    i = i + 2
else:
    print(i, "is no longer exist")


'''-----------------------------------------------
For loop
A for loop is used for iterating over a sequence
that is either a list, a tuple, a dictionary, a set, or a string).

range of function (start, stop, interval)
range(6) = [1,2,3,4,5,6]
-----------------------------------------------'''

for lst in range(6):
    print(lst)

'''-----------------------------------------------
The range() function defaults to 0 as a starting value,
however it is possible to specify the starting value by adding a parameter: range(2, 6),
which means values from 2 to 6 (but not including 6):
-----------------------------------------------'''

for x in range(1, 6):
    print(x, "anuj")

'''-----------------------------------------------
The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
-----------------------------------------------'''

for ls in range(50, 1, -5):
    print(ls, "anuj vaghani")

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc

Fruits = ("Apple", "Mango", "Banana")
for lst in Fruits:
    print(lst, end=" ")

print("")

# Looping Through String

for x in "anuj":
    print(x)

# Break Statement
Fruits = ["Apple", "Mango", "Banana", "Pineapple", "Guava"]
for fal in Fruits:
    print(fal)
    if fal == "Banana":
        break

print("-------------------")

# Continue Statement
for cont in Fruits:
    if cont == "Pineapple":
        continue
    print(cont)


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("Loop is Complete")

# Nested Loop:

Fruit = ["Mango", "Apple", "Banana"]
Vagies = ["Potato", "Tomato", "Carrot"]

for f in Fruit:
    for v in Vagies:
        print(v, f)
