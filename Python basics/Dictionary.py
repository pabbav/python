dict1={1:"fruits", 2:"vegetables",3:"snacks", 4:"deserts"}
for i in dict1.items():
    print(i)
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)
for i,j in dict1.items():
    print(i,j)

######## check this with Teja, why the result is {16, 1, 4, 9} and not {1, 4, 9,1 6}
dict2={i*i for i,j in dict1.items()}
print(dict2)

dict2={i*i:j for i,j in dict1.items()}
print(dict2)

dict1={1:"fruits", 2:"vegetables",3:"snacks", 4:"deserts"}
#print(dict1.get(2))
#print(dict1[2])
#print(dict1.items())
#print(dict1.keys())
#print(dict1.values())
#print(dict1.pop(3))
#print(dict1)
#print(dict1.popitem())
#print(dict1)
#dict1={1:"fruits", 2:"vegetables",3:"snacks", 4:"deserts"}
#dict1.update(4='salad')
print(dict1)
#dict1.update({1:"cookies"})
#print(dict1)

#dict1.update(5:"salad") ---------Not working, chk with Teja, It worked in his machine.
#dict1.update(1='cookies')  ------------#Ans: will work only for characters/variables, as below.
#dict1.update(4,'cake')

#dict1.update(a:"salad")
#dict1.update(b='cookies')
#dict1.update(c,'cake')

dict2={}
list1=[1,2,3]
value1='apple'
print(dict2.fromkeys(list1,value1))

dict1={1:"fruits", 2:"vegetables",3:"snacks", 4:"deserts"}
print(dict1.setdefault(5,'cookies'))

#Assignment
list2=[1,2,3,1,3,2,5,6,3,4,1,0]
dict5={}
for i in list2:
    key=i
    if i in dict5.keys():
        value=dict5.get(i)+1
    else:
        value=1
    dict5.update({key:value})
print(dict5)







