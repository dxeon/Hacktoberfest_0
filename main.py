'''-----------------------------------------------
Arithmatic operators

1) Addition - +
2) Subtraction - -
3) Multiplication - *
4) Division - /
5) Modulo - %
6) Power Operator - **
7) integer division or floor division - //
-----------------------------------------------'''

# Addition
a = 10
a = a + 12
print(a)

# Subtraction
a = 20
a = a - 10
print(a)

# Multiplication
a = 9
a = a * 9
print(a)

# Division
a = 12
a = a / 20
print(a)

# Modulo - Reminder
a = 20
a = a % 3
print(a)

# Power
a = 10
a = a **3
print(a)

# Floor Division
a = 19
a = a // 15
print(a)

print("--------------")

'''-----------------------------------------------
Assignment Operator

1) Addition - +=
2) Subtraction - -=
3) Multiplication - *=
4) Division - /=
5) Modulo - %=
6) Power Operator - **=
7) integer division or floor division - //=
-----------------------------------------------'''

# Addition
a = 10
a += 10
print(a)

# Subtraction
a = 10
a -= 10
print(a)

# Multiplication
a = 10
a *= 10
print(a)

# Division
a = 10
a /= 10
print(a)

# Modulo - Reminder
a = 20
a %= 3
print(a)

# Power
a = 10
a **= 10
print(a)

# Floor Division
a = 10
a //= 10
print(a)

print("--------------")

'''-----------------------------------------------
Comparision operators

1) Equals to - ==
2) Not Equals to - !=
3) Less then - <
4) Greater then - >
5) Less then Greater then - >=
6) Greater then Greater then - <=
-----------------------------------------------'''

print(9 == 5)
print(9 != 5)
print(9 > 5)
print(8 < 5)
print(5 >= 5)
print(5 <= 5)

print("--------------")

'''-----------------------------------------------
Logical operators

1) And - &
2) Or - |
3) Not - !

-----------------------------------------------
AND Truth Table
A  B  O/P
0  0  0
0  1  0
1  0  0
1  1  1

OR Truth Table
A  B  O/P
0  0  0
0  1  1
1  0  1
1  1  1

XOR Truth Table
A  B  O/P
0  0  0
0  1  1
1  0  1
1  1  0
-----------------------------------------------'''

a = 5
b = 3
c = 2

print(a & b)
print(a | b)
print("? = ", not(0))

print(a < b & b < c)
# false & false = false

print(a > b | b > c)
# ture | false = true

print("--------------")

'''-----------------------------------------------
Identity operators

1) is 
2) is not

-----------------------------------------------'''

a = 5
b = 10

print(a is b)
print(b is not a)

print("--------------")

'''-----------------------------------------------
Membership operators

1) in 
2) not in
-----------------------------------------------'''

a = [1, 3, 5, 76, 8, 54, 12, 412, 4, 8]

print(2 in a)
print(5 not in a)

print("--------------")

'''-----------------------------------------------
Bitwise operators

1) Bitwise AND - &
2) Bitwise OR - |
3) Bitwise XOR - ^
4) Bitwise NOT / Compliment - ~
5) Left Shift - <<
6) Right Shift - >>
-----------------------------------------------'''

print(~12)

''' Logic Of Bitwise NOT / Compliment :-
	Binary of 12 is -----------------> 00001100
	compliment of that binary id ----> 11110011 
	11110011 this is 2's compliment of -13
'''

print(12 & 13)

''' Logic Of Bitwise AND :-
	Binary of 12 is -----------------> 1100
	Binary of 13 is -----------------> 1101 
	see turth table of AND and output binary's decimal number is answer
'''

print(12 | 13)

''' Logic Of Bitwise OR :-
	Binary of 12 is -----------------> 1100
	Binary of 13 is -----------------> 1101 
	see turth table of OR and output binary's decimal number is answer
'''

print(12 ^ 13)

''' Logic Of Bitwise XOR :-
	Binary of 12 is -----------------> 1100
	Binary of 12 is -----------------> 1101 
	see turth table of XOR and output binary's decimal number is answer
'''

print(10 << 2)

''' Logic Of Left Shift :-
	Binary of 10 is -----------------> 1010
	actully we have 1010.0000  
	now we want to left shift 2.. it means shift 2 zeros to left size
	now it is 101000.00 and go with normal calculation to convert binary to decimal
	so 32 + 8 = 40. so our ans is 40.
'''

print(10 >> 2)

''' Logic Of Right Shift :-
	Binary of 10 is -----------------> 1010
	actully we have 1010.0000
	now we want to right shift 2.. it means shift 2 digits to right size from dot
	now it is 10.10 and go with normal calculation to convert binary to decimal
	so binary of 10 is 2. so our ans is 2.
'''

'''
Binary Numbers
0 - 0000
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
6 - 0110
7 - 0111
8 - 1000
9 - 1001
10 - 1010
11 - 1011
12 - 1100
13 - 1101
14 - 1110
15 - 1111
'''
