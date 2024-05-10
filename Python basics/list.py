#slicing
list1=[1,2,3,4,5]
print(list1[:3:2])

#list reversal without methods
list2=[1,4,8,2,6]
for i in list2:
    list3=list2[::-1]
    break
print(list3)

#list methods
studentmarks=[70,90,98,85,74,86]

#append-object-Element passed as argument is appended to end of list.Length of the list increases by 1.
studentmarks.append(89)
studentmarks.append([78,98])
print(studentmarks)

#extend-iterable-Element passed as argument is appended to end of list.Length of list increases by no. of elements in iterable.
studentmarks.extend([56])
studentmarks.extend([92,98])
print(studentmarks)

#copy
studentmarks2=studentmarks.copy()
print(studentmarks2)

#pop
studentmarks.pop(3)
print(studentmarks)

#count
print(studentmarks.count(98))

#index
print(studentmarks.index(98))
print(studentmarks.index(98,3,5))

#sort
print(studentmarks.sort())
print(studentmarks.sort(reverse=True))

#insert
studentmarks.insert(5,89)
print(studentmarks)

#remove
studentmarks.remove(85)
print(studentmarks)

#reverse
studentmarks.reverse()
print(studentmarks)











