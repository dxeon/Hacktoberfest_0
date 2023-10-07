'''
try__except__else__finally

try: It is only mandatory clause in exception handling.try runs first in try__except

except: if python runs into an exception, then code present in exception will run.

else:  if try is successfully executed then after execution of try block else part will execute.

finally:  this part always runs.
'''

# ex.1
#This program should take int input only
x = int(input('Enter a number'))
print(x)

try:
	x = int(input('Enter your number'))
	print(x)
except:
	print('Enter a valid integer number')

# ex.2
try:
	x = int(input('Enter a number: '))
	print(x)
except:
	print('Enter a valid number')
else: #it will run if try successfully run
	print('Try Successfully Run..')
finally:  #this will obviously run
	print('your task is done!')

# ex.3
x = int(input('Enter a number'))
y = int(input('enter a number'))
z = x/y
print(z)

try:
	x = int(input('Enter a number'))
	y = int(input('enter a number'))
	z = x/y
	print(z)
except ZeroDivisionError:
	print('You are dividing number by zeros')
except ValueError:
	print('Enter a valid integer number')
except KeyboardInterrupt:
	print('keyboard interrupt')


# ex.4
try:
	x = int(input('no: '))
	print(x)
except (ValueError,ZeroDivisionError,KeyboardInterrupt):
	print('not a valid number or you are dividing value by 0 or you pass the keyboard interrupt') 
	
# ex-5
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")

#ex-6
def fun(a):
    if a < 4:
  
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
  
    # throws NameError if a >= 4
    print("Value of b = ", b)
      
try:
    fun(3)
    fun(5)
  
# note that braces () are necessary here for 
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

#ex-7
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
