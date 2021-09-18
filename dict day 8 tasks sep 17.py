#DICTIONARIES
>>>d1={12,23,45,23}
>>> d2={'name':'abdul','age':26.3,'branch':'cse'}
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'abdul'
>>> d2.get('age')
26.3
>>> d2['rollno']=123
>>> d2
{'name': 'abdul', 'age': 26.3, 'branch': 'cse', 'rollno': 123}
>>> d2['age']=27
>>> d2
{'name': 'abdul', 'age': 27, 'branch': 'cse', 'rollno': 123}
>>> d2.keys
<built-in method keys of dict object at 0x000002441004B700>
>>> d2.keys()
dict_keys(['name', 'age', 'branch', 'rollno'])
>>> d2.values()
dict_values(['abdul', 27, 'cse', 123])
>>> d2.items()
dict_items([('name', 'abdul'), ('age', 27), ('branch', 'cse'), ('rollno', 123)])
>>># items will return with list of tuple
>>> d2.pop('age')
27
>>> d2
{'name': 'abdul', 'branch': 'cse', 'rollno': 123}
>>> d2.popitem()
('rollno', 123)
>>> d2
{'name': 'abdul', 'branch': 'cse'}
>>> d2.update()
]
>>> d2
{'name': 'abdul', 'branch': 'cse'}
>>> d2.update()
>>> d2
{'name': 'abdul', 'branch': 'cse'}
>>> d2.update({'branch':"ece"})
>>> d2
{'name': 'abdul', 'branch': 'ece'}
>>> marks={}.fromkeys(["c","cpp","python","java"],0)
>>> marks
{'c': 0, 'cpp': 0, 'python': 0, 'java': 0}
>>> #it will create of list of keys with single values
>>> d2.setdefault(" email","hemasree@gmail.com")
'hemasree@gmail.com'
>>> d2
{'name': 'abdul', 'branch': 'ece', ' email': 'hemasree@gmail.com'}
>>> d2.setdefault("branch","eee")
'ece'
>>> d2
{'name': 'abdul', 'branch': 'ece', ' email': 'hemasree@gmail.com'}
>>> 

#TASKS
#1>write a program to add a key-value pair to the dictionary
d={}
n=int(input("enter"))
for i  in range(n):
    keys=(input("enter key"))
    values=(input("enter value"))
    d[keys]=values
print(d)
output:
enter3
enter keyhell
enter value0
enter keyheaven
enter value1
enter keypeace
enter value100
{'hell': '0', 'heaven': '1', 'peace': '100'}
#
d1={"apple":3,"mango":4,"banana":6}
key=input("Enter the key to be added:")
value=int(input("Enter the value for the key to be added:"))

d1.update({key:value})
print("Updated dictionary is:")
print(d1)


output:
Enter the key to be added:hema
Enter the value for the key to be added:4
Updated dictionary is:
{'apple': 3, 'mango': 4, 'banana': 6, 'hema': 4}


#2>program to concatenate two dictionaries into one
d1={"apple":3,"mango":4,"banana":6}
d2={"square":4,"triangle":5,"circle":6}
d1.update(d2)
print("concatenate dictornary:",d1)

output:
concatenate dictornary: {'apple': 3, 'mango': 4, 'banana': 6, 'square': 4, 'triangle': 5, 'circle': 6}

#3>Python Program to Check if a Given Key Exists in a Dictionary or Not

k=input("enter the key:")
d2={"square":4,"triangle":5,"circle":6}
if k in d2.keys():
    print("present in dictornary",d2[k])
else:
    print("isn't present:")
    

output:
enter the key:circle
present in dictornary 6

enter the key:rect
isn't present

#4>write a program to generate a dictionary that contains numbers(between 1 and n )in the form(x*x*x)
n=int(input("enter the value:"))
d={}
for i in range(n):
    d.setdefault(i,i*i)
print(d)

output:
enter the value:4
{0: 0, 1: 1, 2: 4, 3: 9}
#other way
n=int(input("enter the value:"))
d={}
for i in range(1,n+1):
    d[i]=pow(i,2)
print(d)

output:
enter the value:5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



#5>Python Program to Sum All the Items in a Dictionary


d2={"square":4,"triangle":5,"circle":6}
print("total sum of the items:",sum(d2.values()))


output:
total sum of the items: 15

#6>Python Program to multiply All the Items in a Dictionary


d1={"apple":3,"mango":4,"banana":6}
m=1
for i in d1:
    m=m*d1[i]
print("multiply all the items:",m)


output:
multiply all the items: 72


#7>Python Program to remove the given key from a Dictionary


d1={"apple":3,"mango":4,"banana":6}
m=1
k=input("enter the value:")
if k in d1:
    d1.pop(k)
print("updated dict:",d1)

output:
enter the value:banana
updated dict: {'apple': 3, 'mango': 4}


#8>Python Program to Map Two Lists into a Dictionary
d1=[]
d2=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    keys=input("Enter element:")
    d1.append(keys)
print("For values:")
for x in range(0,n):
    values=int(input("Enter element:"))
    d2.append(values)
d=dict(zip(d1,d2))
print("The dictionary is:")
print(d)

output:
Enter number of elements for dictionary:4
For keys:
Enter element:A
Enter element:B
Enter element:C
Enter element:D
For values:
Enter element:1
Enter element:2
Enter element:3
Enter element:4
The dictionary is:
{'A': 1, 'B': 2, 'C': 3, 'D': 4}

#9>python program to count the frequency of words appearing in a string using a dictionary
words=input().split()
wordscount={}
print(len(words))
for word in words:
    wordscount[word]=words.count(word)
print(wordscount)
uniqwords=list(set(words))

output:
i am hema and i am from vzm and i am working in css
14
{'i': 3, 'am': 3, 'hema': 1, 'and': 2, 'from': 1, 'vzm': 1, 'working': 1, 'in': 1, 'css': 1}

#to reduce the iteration
words=input().split()
wordscount1={}
print(len(words))
for word in words:
    wordscount1[word]=words.count(word)
print(wordscount1)

wordscount2={}
uniqwords=list(set(words))
print(len(uniqwords))
for word in uniqwords:
    wordscount2[word]=words.count(word)
print(wordscount2)

output:
i am hema and i am from vzm and i am working in css
14
{'i': 3, 'am': 3, 'hema': 1, 'and': 2, 'from': 1, 'vzm': 1, 'working': 1, 'in': 1, 'css': 1}
9
{'i': 3, 'am': 3, 'from': 1, 'vzm': 1, 'css': 1, 'in': 1, 'hema': 1, 'working': 1, 'and': 2}


#10>python program to create a dictionary with key as first character and value as words starting with that character 
words=input("Enter string:")
l=words.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)

        
output:
Enter string:hema is super expert in python programming skills
h : ['hema']
i : ['is', 'in']
s : ['super', 'skills']
e : ['expert']
p : ['python', 'programming']



