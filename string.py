# Strings

current_year = 2019
birth_year = 1998
age = current_year - birth_year
print("Age:",age)

# Strings Accept
'''
current_yar
_birth_year_
myVar
MYVAR
_myVar34sd23
MyVar
'''

#Strings Not Accept
'''
My var =  
3hdgs = 
hjc-+zbcs
'''

a = b = c = 10
print(a,b,c)
print(a+b+c)

x = 'Harsh'
print(x[2])

'''-----------------------------------------------
rstrip() - It removes white space
-----------------------------------------------'''
y = "Harsh Dalwadi  "
print(y.rstrip())

'''----------------------------------------------------
strip() - It removes white space from beginning and end
----------------------------------------------------'''
a = "   Anuj Vaghani "
print(a.strip())

'''-----------------------------------------------
upper() - Covert all text into upper case
-----------------------------------------------'''
a = "Anuj Vaghani"
print(a.upper())

'''-----------------------------------------------
lower() - Covert all text into lower case
-----------------------------------------------'''
a = "Anuj Vaghani"
print(a.lower())

'''-----------------------------------------------
title() - Covert first letter capital from all words
-----------------------------------------------'''
a = "harsh dalwadi"
print(a.title())

'''-----------------------------------------------
capitalize() - Covert first letter capital
-----------------------------------------------'''
a = "Anuj Vaghani"
print(a.capitalize())

'''-----------------------------------------------
replace(original,change) - replace word 
-----------------------------------------------'''
a = "Anuj Vaghani"
print(a.replace("Dalwadi","prajapati"))

'''-----------------------------------------------
Split() - Split Word From specified place
-----------------------------------------------'''
a = 'My_name_is_Harsh'
print(a.split(sep="_"))

a = "Hello, World!"
print(a.split(","))

'''-----------------------------------------------
len() - Find length
-----------------------------------------------'''
a = "Harsh Dalwadi"
print(len(a))

'''-----------------------------------------------
print(a[::]) - Print from through and with intervals
-----------------------------------------------'''
a = "abcdefghijklmnopqrstuvwxyz"
print(a[3:10:2])

'''-----------------------------------------------
isnumeric() - Check sentense is numeric or not
-----------------------------------------------'''
a = "12345674"
print(a.isnumeric())

'''-----------------------------------------------
isalpha() - Check sentense is alphabetical or not
-----------------------------------------------'''
a = "Harsh"
print(a.isalpha())

'''-----------------------------------------------
isalnum() - Check sentense is alphanumeric or not
-----------------------------------------------'''
a = "Harsh8"
print(a.isalnum())

'''-----------------------------------------------
Concate String
-----------------------------------------------'''
a = "Harsh"
b = "Dalwadi"
c = "H."
print(a+c+b)
print(a,b,c)

'''-----------------------------------------------
Word or letter is in the sentence or not
-----------------------------------------------'''
m = '''str() - constructs a string from a wide variety of data types, including
strings, integer literals and float literalsCasting in python is therefore
done using contructor functions:int() - constructs an integer number from an
integer literal, a float literal (by rounding down to the previous whole
number), or a string literal (providing the string represents a whole
number)float() - constructs a float number from an integer literal, a float
literal or a string literal (providing the string represents a float or an
integer)str() - constructs a string from a wide variety of data types,
including strings, integer literals and float literalsExample'''

print("con" in m)
print("hars" not in m)

'''-----------------------------------------------
Change word via external 
-----------------------------------------------'''
#global

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# user input

a = int(input("Enter value of Pen: "))
b = int(input("Enter Value of Pencil: "))

print("value of pen is {} and pencil is {}".format(a,b))

'''-----------------------------------------------
Escape Character
-----------------------------------------------'''
txt = "We are the so-called "Vikings" from the north." #try
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

'''-----------------------------------------------
Is true or not?
-----------------------------------------------'''
print(10 != 9)


# \n	New Line
# \t	Tab
new_str = input("enter your string: ")

for x in new_str:
  print(x)
