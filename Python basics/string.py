#string methods
str1="Good Morning"

list1=str1.split(" ") #split - returns list
print(list1) # list1 is iterable

list2=" ".join(list1)#join - requires iterable
print(list2)

str6=''' Hello
This is Python class
Good Morning'''
print(str6.splitlines())

print(str1.find("o"))
print(str1.find("o",4,8))

str2="$$Good Morning$$"
print(str2.lstrip("$"))
print(str2.rstrip("$"))
print(str2.strip("$"))

str3="  $$Good Morning$$"
str4=(str3.strip()).lstrip("$")
print(str4)

str5="one day at a time"
print(str5.capitalize())
print(str5.title())

str6="You need {} to unlock {}"
print(str6.format('keys', 'door'))

str6="You need {0} to unlock {1}"
print(str6.format('keys', 'door'))

str6="You need {1} to unlock {0}"
print(str6.format('keys', 'door'))

str6="You need {k} to unlock {d}"
print(str6.format(d='keys', k='door'))

#Formatting string using % Operator
str1="This is python %s and I am paying for %s and cost is %d"%("class","class",25000)
print(str1)

#floating precision
result=3.141592
print(result)
print("%5.9f" %(result))

#{[index]:[width][.precision][type]}??????? what does this comment line this mean??
var ="class"
str4=f"This is python {var}"
print(str4)

str1="Today is tuesday"
print(str1.swapcase())
print(str1.index('d'))
print(str1.index('d',8,15))
print(str1.count("d"))
print(str1.count("d",0,5))
print(str1.upper())
print(str1.endswith('ay'))
print(str1.endswith('is',1,7))
print(str1.upper())
print(str1.lower())
#casefold- it converts all charecters into lower case
str1="helloiamlDFGDGDGearningpython"
result=str1.casefold()
print(result)

#center  - method will center align the string using specified character , space is default
str1="g"
result=str1.center(7,'O')
print((result))

#isalnum---
str1="version32455rfsdf"
result=str1.isalnum()
print(result)

# isdigit - return True if string has all digit else False
str1="123445353&34%$"
result=str1.isdigit()
print(result)

#isalpha - retunr True if string has all alphabhates letters
str1="helloiamlearningpython"
result=str1.isalpha()
print(result)

#isnumeric--- check if all characters in string are numaric
str1="576778.88"
result=str1.isnumeric()
print(result)

#istitile --- check if given string in title format
str1="HEllo And Welcome"
result=str1.istitle()
print(result)

#islower - it will check string in lower caseornot
str1="AmuLS ACADEmY"
result=str1.islower()
print(result)

#isupper -  it will check string in upper case or not
str1="ACADE"
result=str1.isupper()
print(result)

#isspace --- check if all characters in the strign are whitespaces
str1="66868    979"
result=str1.isspace()
print(result)

#isidentifier----  check if the strign is identifier or variables
str1="22Demo343"
result=str1.isidentifier()
print(result)

str2=str1.replace('d',"D")
print(str2)

str2="today is tuesday"
for i in str2:
  print(i, end=' ')
print(" ")

print(len(str2))
print(len(str2[0:5]))

str2="today is tuesday"
print(str2[-5:-2])
print(str2[:8])

# This value is the memory address of the object and will be different every time you run the program
print(id(str2))

a=9
b="this is pythn"
print(str(a)+b)

mystr1='This'
mystr2=' is python'
print(mystr1+mystr2)

list1=[1,2,3,44]
#print(type(list1))
b=str(list1)
print(b)
print(type(b))

#iteration Through a string
letter1="i am manikanta"
for i in letter1:
    print(i, end=',')
print(" ")
list1=[1,4,2,2,6,3,6,3,5]
for i in list1:
    if i==2:
        print("true")
print(letter1)

# find
itestring='hello ramya'
count=0
for letter in itestring:
    if letter=='a':
        count=count+1
print(count)
print(itestring, end=',')

n=1
print("hello"+str(n))

str1="This is p\"ython"
print(str1)
print(str1[6])

print('''He said, "What's there?"''')
print('He said, "What\'s there?\"')

str2="either sine"
str1="either sune"
print(str1==str2)

###########Tasks#############
#1.create string and print individual elemnets separateed by '_' ex: python o/p:p_y_t_h_o_n_
str1="Python"
for i in str1:
  print(i,end='_')

#2.create string and print each elements twice and separtaed by $ ex:python o/p:pp$yy$tt$hh$oo$nn$
str1="Python"
for i in str1:
  str2=str(i)+str(i)
  print(str2, end='$')

#3.sumofdigits function
def sumofdigit(n):
  sum = 0
  while n > 0:
    r = n % 10  # 7 #9 #8
    sum = sum + r  # 7 #16 # 24
    n = n // 10  # 89 #8 #0
 # return sum
  print(sum)

sumofdigit(89809)

#Encode---????????????
str1='This is python  this is python'
result=str1.encode('ASCII')
print(result)
result.decode()
print(result)

str1="H\te\tl\tl\to"
print(str1)
print(str1.expandtabs(2))

str6="You need {} to unlock {}"
print(str6.format('keys', 'door'))

str1 = {'x':'Apple', 'y':'Banana'}
print("{x} is Sweet and {y} is raw".format_map(str1))

str2="today is tuesday"
str3=str2.partition('tuesday')
print(str3)

str2="today is tuesday"
str3=str2.partition(' ')
print(str3)

str2="today is tuesday"
print(str2.ljust(20), "it is hot")
print(str2.rjust(20), "it is hot")
print(str2.isprintable())

str2="50"
print(str2.zfill(10))

str2= 'today is tuesday'
print(str2.removeprefix('today'))

str2= 'today is tuesday'
print(str2.removesuffix('day'))

var = "Geeks for Geeks"
print(var.startswith("Geeks"))
print(var.startswith("Hello"))

str2= 'today is tuesday'
print(str2.rindex('is',5,8))

str2= 'today is tuesday'
print(str2.rfind('tuesday'))

str2= 'today is tuesday'
print(str2.rjust(20,'*'))

str2= 'today is tuesday'
str3=str2.maketrans("t", "a")
print(str2.translate(str3))

str1="hello guys and welcome"
dic1={"a":"1","b":"2","c":"3","d":"4"}
table=str1.maketrans(dic1)
print(table)

print(ord('u'))
print(chr(117))

str1="Hello"
print(str1[::-1])











