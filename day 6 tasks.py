#1>Python Program to Replace all Occurrences of ‘a’ with $ in a String
n=input("enter string")
print("the replaced lettef is:")
n=n.replace('a','$')
print(n)

output:
enter stringbanana
the replaced lettef is:
b$n$n$


#2>Python Program to Detect if Two Strings are Anagrams
s1=input("enter 1st string:")
s2=input("enter 2nd string:")
if(sorted(s1)==sorted(s2)):
     print(s1+ " and " +s2+ " are anagrams")
else:
       print(s1+ " and " +s2+ " are not anagrams")
       
output:
enter 1st string:race
enter 2nd string:care
race and care are anagrams


#3>Python Program to Count the Number of Vowels in a String
s1=input("enter string:")
vowels=0
s2=s1.upper()
for i in s2:
    if(i=='A' or i=='E' or i=='I' or i=='0' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels+=1
print("number vowels in this string:",vowels)

output:
enter string:hemasree
number vowels in this string: 4

#4>Python Program to Form a New String where the First Character and the Last Character have been Exchanged
s1=input("enter a string")
start=s1[0]
cont=s1[1:-1]
end=s1[-1]
print("the exchanged new string is:",end+cont+start)
output:
enter a string conzura
the exchanged new string is: aonzurc
 
#5>Python Program to Take in a String and Replace Every Blank Space with Hyphen
x=input("enter string:")
str=x.replace(' ','-')
print(str)
output:
enter string:hema sree
hema-sree

#6>Python Program to Calculate the Length of a String Without Using a Library Function
x="conzura soft solutions"
count=0
for i in x:
    count+=1
print(count)
output:22

#7>Python Program to Calculate the Number of Words and the Number of Characters Present in a String
x=input("enter string:")
words=x.split()
print(words)
print(len(words),len(x))
output:
enter string:conzura soft solutions
['conzura', 'soft', 'solutions']
3 22


#8>Python Program to Count Number of Lowercase Characters in a String
x=input("enter a string")
count=0
for ch in x:
    if(ch.islower()):
        count+=1
print(count)
output:
enter a stringHemASree
5



#9>Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
x=input("enter a string")
y=input("enter a string1")
count1=0
count2=0
for ch1 in x:
    count1+=1
for ch2 in y:
    count2+=1
if(count1>count2):
    print("larger is :",x)
elif(count1==count2):
    print(x+ " and " +y+ " are equal")
else:
    print("larger is:",y)

output:
enter a stringhemasree
enter a string1conzura
larger is : hemasree

enter a stringpyuthon
enter a string1conzura
pyuthon and conzura are equal


#10>Python Program to Check if a String is a Palindrome or Not
s=input("enter string:")
if(s==s[::-1]):
    print(s+ "  is palindrome")
else:
    print(s+" is not a palindrome")
output:
enter string:level
level  is palindrome
>>> 


#11>Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
s=input("enter string:")
count1=0
count2=0
for i in s:
    if(i.islower()):

        count1+=1

    elif(i.isupper()):
        
    
        count2+=1
print("lowercae  are:",count1)
print("upper case are:",count2)
output:
enter string:COnzura SofT SoluTions
lowercae  are: 14
upper case are: 6


#12>Python Program to Calculate the Number of Digits and Letters in a String
s=input("enter")
count1=0
count2=0
for i in s:
    if (i.isalpha()):
        count1+=1

    elif(i.isdigit()):
        
    
        count2+=1
print("letters  are:",count1)
print("digits are:",count2)
output:
enter hema1234sree8775
letters  are: 8
digits are: 8


#13>Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
p=input("enter:")
x=p[:2]
y=p[-2:]
print("new string:",x+y)
output:
enter:hemasree
new string: heee
    
    

#14>Python Program to Count the Occurrences of Each Word in a Given String Sentence
s=input("enter the string")
x=s.split()
a=[]
for i in x:
    if (i not in a):
          a.append(i)
    

for i in range(0,len(a)):
    print("occurrence of:",a[i],"is:",x.count(a[i]))
output:
enter the stringhema is a smart hema
occurrence of: hema is: 2
occurrence of: is is: 1
occurrence of: a is: 1
occurrence of: smart is: 1
    
#15>Python Program to Check if a Substring is Present in a Given String
s=input("enter the string")
x="hema"
if (s not in x):
          
          print(s," is not a substring")
else:
         print(s, " is a substring")

output:
enter the stringconzura soft solutions
conzura soft solutions  is not a substring


#16
s="hguyg456"
sum=0
for ch in s:
    if ch.isdigit():
       sum+=int(ch)
print("add",sum)
output:
add 15





 



    
    








 
