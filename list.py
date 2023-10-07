'''-----------------------------------------------
List - Mutable - []
-----------------------------------------------'''
lst = ["Harsh","Jimit","Aalap","Vishnu","Nisarg","Lay",3,4,3.4]
print(lst)

#Access Items [start:end+1:interval]
print(lst[1:5:2])

#Change Element
lst[2] = " prince patel"
print(lst[3])

#Check Length of List
print(len(lst))

#Add Value in List [append element at last]
lst.append(["Laxman","Dalwadi"])
print(lst)

#Add value at specified place (index , value)
lst.insert(4,"Harsh Dalwadi")
print(lst[4])

#delete particular element
lst.remove("Harsh Dalwadi")
print(lst)

#delete element at last from list
lst.pop()
print(lst)

#delete element from particular index
del lst[0]
print(lst)

# python all list methods

append() => Adds an element at the end of the list
clear()	=> Removes all the elements from the list
copy()	=> Returns a copy of the list
count()	=> Returns the number of elements with the specified value
extend()	=> Add the elements of a list (or any iterable), to the end of the current list
index()	=> Returns the index of the first element with the specified value
insert()	=> Adds an element at the specified position
pop()	=> Removes the element at the specified position
remove()	=> Removes the first item with the specified value
reverse()	=> Reverses the order of the list
sort()	=> Sorts the list

#delete whole list
# del lst
# print(lst)

#empty list
lst.clear()
print(lst)

#Copy list
#Method 1
Numbers = (1,2,3,4,5,6,7,8,9)
print(Numbers)
print(type(Numbers))
lst1 = list(Numbers)
print(lst1)
#Method 2
lst = lst1.copy()
print(lst)

#Concate two list
x = [1,2,3,4,3]
y = ["Harsh","Jimit","Aalap",]
z = x + y
print(z)

#Other way to concate list
# x.extend(y)
# print("Y = ",y)
# print("X = ",x)
y.extend(x)
print("Y = ",y)
print("X = ",x)


#Reverse List
x.reverse()
y.reverse()
print(x)
print(y)

#ex-7
thislist = ["apple", "banana", "cherry"]
print(thislist)
