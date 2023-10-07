'''-----------------------------------------------
If Statement:
An if statement is a conditional statement that runs or skips code based on
whether a condition is true or false.

syntax :

if condition:
	...code...
-----------------------------------------------'''

a = 40
b = 20

if a < b:
    print("b is greater")

'''-----------------------------------------------
If else Statement:
syntax : 

if condition:
	...code...
else:
	...code...
-----------------------------------------------'''

a = 30
b = 40

if a < b:
    print("A is Small")

else:
    print("A is Big")

print("-----------------------------------------------")

# Program

phone_balance = int(input("Enter Phone balance: "))
bank_balance = 500

print("Current Phone balance is:", phone_balance)
print("Current Bank balance is:", bank_balance)

if phone_balance <= 10:
    bank_balance -= 100
    phone_balance += 100
    print("After Transition Balances are..")
    print("Phone balance: ", phone_balance)
    print("Bank balance: ", bank_balance)

else:
    print("You have efficient balance to call someone")


print("-----------------------------------------------")

'''-----------------------------------------------
If elif Statement:
syntax :

if condition:
	...code...
elif condition:
	...code...
else:
	...code...
-----------------------------------------------'''

a = 1
b = 2
c = 3

if a < b and a < c:
    print("a is sml")

elif b < c and b < a:
    print("b is small")

else:
    print("c is small")

print("-----------------------------------------------")

# Program

bank_balance = 1000
phone_balance = int(input("Enter your Phone balance : "))

if phone_balance <= 20:
    print("You don't have efficient balance to make call!")
    if bank_balance < 50:
        print("You don't have sufficient bank balance")
    else:
        phone_balance += 50
        bank_balance -= 50
        print("Updated Phone balance: ", phone_balance)
        print("Updated Bank balance: ", bank_balance)

elif phone_balance > 20 and phone_balance < 500:
    ask = input("Do you want to recharge your phone(Y/N): ")
    if ask == "y" or ask == "Y":
        do_balance = int(input("Enter recharge amount: "))
        if do_balance < bank_balance:
            phone_balance += do_balance
            bank_balance -= do_balance
            print("Updated Phone balance: ", phone_balance)
            print("Updated Bank balance: ", bank_balance)
        else:
            print("You don't have sufficient bank balance")

    elif ask == "n" or ask == "N":
        print("No Problem!")
        print("You have efficient balance to make a call")
        print("Phone balance: ", phone_balance)
        print("Bank balance: ", bank_balance)


elif phone_balance >= 500:
    print("You have efficient balance")


else:
    print("Please Enter Right input")

print("Thank You!")
print("-----------------------------------------------")

'''-----------------------------------------------
Shorthand if
-----------------------------------------------'''
a = 10
b = 20

if a <= b:
    print("a is small")

'''-----------------------------------------------
Shorthand if else

technique of writing if_else is also known 
as ternary operator or
-----------------------------------------------'''

print("a is big") if a > b else print("b is big")

'''-----------------------------------------------
Pass - if we want to write code later..that time 
we can use pass instead of code
-----------------------------------------------'''

if a <= 10:
    pass

else:
    print("OK")
