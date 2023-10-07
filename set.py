'''
SET
-> Unordered collection of elements
-> order of elements is not maintained in the sets
-> No duplication allowed
-> Mutable - so we can modify it.
-> Unordered - we can not access it through a[?].
-> representation - {}
-> ex. a = { 10, 20, 'python', 20.6 }
-> When use : Avoid Repeatation and no access thorugh index
'''

# Presentation
a = { 10, 20, 'python', 20.8}
print(a)
print(type(a))
print('id: ',id(a))

# No Repeat
a = { 10, 20, 'python', 20.6, 10, 55}
print(a)

# Create Empty set
a = set()

# Set Methods
a = {'python','java','c','c++','IOT'}
b = {'AI','ML', 'java','Data Science','IOT', 'Big Data','c','c++'}

print('A: ',a)
print('B: ',b)

#1 intersection - common in both
inter = a.intersection(b)
print('Intersection: ',inter)

#2 Union - Return all items from all sets
uni = a.union(b)
print('Union: ',uni)

#3 Difference - Return uncommon values
diff1 = a.difference(b)
print('Uncommon in a: ',diff1)
diff2 = b.difference(a)
print('Uncommon in b: ',diff2)

#4 Subset - all elements of a are in the b
sub = a.issubset(b)
print('Subset: ',sub)

#5 Superset - Elements of B are in A
sup = a.issuperset(b)
print('Superset: ',sup)

# a.intersection_update(b)
# a.difference_update(b)

#Add Elements
a = {'Nisarg','Aalap','Jimit'}
a.add('anuj')
print(a)


#Update Multiple Elements - it can be list, tuple
a.update([22,34,56])
a.update(('HD','AM'))
print(a)

#copy set elements - new_set = set_name.copy()
h = a.copy()
print("H:",h)

#Removing Elements
h.remove('Harsh')
h.discard('prince')
print(h)
h.clear() #clear all elements
print("After Clear")
