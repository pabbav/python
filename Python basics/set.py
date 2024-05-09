#empty set declaration using set()
set1=set()
print(type(set1))

# creating set with values using set()
set1=({1,2,3.4,'a','jkj'})
print(set1)

#another way
set1={1,2,3.4,'a','jkj'}

#set with values
set2={2,'hello',5.6, 'a'}
print(set2)

#set hetrogenous elements.Duplicates will be removed.
myset={1.0, "Hello", (1, 2, 3),2.6,2.6}
print(myset)

#Diff. between list, tuple, set
#Duplicate values are not allowed in set
letters='dgfgjhhihkjhiFYGUGUJHIUHI'

list_letters=list(letters)
print(list_letters)

tuple_letters=tuple(letters)
print(tuple_letters)

set_letters=set(letters)
print(set_letters)

#set cannot have mutable object.
#set cannot have sets,dictionary,list
my_set = {1, 2, (3, 4)}
print(my_set)

my_set = {1, 2, (3, 4),[1,2]}
print(my_set)

my_set = {1, 2, (3, 4), {6,7}}
print(my_set)

#accessing elements in set
#since it is unordered collection, indexing is not possible.
set1={1,2,3,4,5,6,7}
for i in set1:
    print(i)

#set methods
set1={1,2,3,4,5,6,7,8,9}
set1.add(34)
print(set1)

#To add more than one value.
set1={1,2,3,4,5,6,7,8,9}
set1.update([1,2,53,54,4])
print(set1)

my_set1 = {1, 3}
my_set1.update([4, 5], {1, 6, 8},(1,2,45,3))
print(my_set1)

# discard leaves set unchanged  and remove will raise an error in such a condition.
set1={1,2,3,4,5,6}
set1.discard(51)
print(set1)

set1={1,2,3,4,5,6}
set1.remove(51)
print(set1)

#membership operator
myset1 = {'a', 'l', 'p', 'e'}
print('a' in myset1)
print('p' not in myset1)

#union
A = {1,2,3,4,5,7}
B = {6,9,11,12,13}
print(A|B)  # or
print(A.union(B))

#intersection
A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A & B)  #and
print(A.intersection(B))

#Difference
A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A-B)
print(A.difference(B))

A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(B-A)
print(B.difference(A))

#Symmetric difference
A = {1,2,3,4,5,7}
B = {4,5,6,8,8,6}
print(A^B)
print(A.symmetric_difference(B))

#Difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
print(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.difference_update(x)
print(x)
print(y)

#pop will remove arbitrary value
set1={1,2,3,4,5}
set1.pop()
print(set1)

#clear method clears values in set and displays empty set
set2={1,2,3,4,5}
set2.clear()
print(set2)




