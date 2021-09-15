#you have to implement a log to perform all arithmetic operations
a=int(input("enter a:"))
b=int(input("enter b:"))
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a%b)
print("mod:",a/b)
print("approximate:",a//b)
print("power:",a**b)
print("(a+b)+b):",(a+b)+b)
print("(a+b*b):",(a+b*b))

output:
enter a:3
enter b:5
add: 8
sub: -2
mul: 15
div: 3
mod: 0.6
approximate: 0
power: 243
(a+b)+b): 13
(a+b*b): 28


#write a program to find biggest of 2 numbers
n1=int(input("enter the number n1:"))

n2=int(input("enter the number n2:"))
if (n1>n2):
    print("n1 is biggest number ")
else:
    print("n2 is biggest number ")
       
output:
enter the number n1:45
enter the number n2:7
n1 is biggest number


#write a program to find biggest of 3 numbers
n1=int(input("enter the number n1:"))

n2=int(input("enter the number n2:"))
n3=int(input("enter the number n3:"))
if (n1>n2) and (n1>n3):
    print("n1 is biggest number ")
elif(n2>n1) and (n2>n3):
    print("n2 is biggest number ")
else:
    print("n3 is biggest  number:")
    
       

output:
enter the number n1:23
enter the number n2:55
enter the number n3:2
n2 is biggest number 


#wrie a program to print numbers in a given range
initial=int(input("enter the initial value:"))
final=int(input("enter the final value:"))
for i in range(initial,final+1):
    print("the given range of values are:"i)


output:
==================== RESTART: C:\Users\HP\Desktop\anagram.py ===================
enter the initial value:4
enter the final value:22
the given range of values are: 4
the given range of values are: 5
the given range of values are: 6
the given range of values are: 7
the given range of values are: 8
the given range of values are: 9
the given range of values are: 10
the given range of values are: 11
the given range of values are: 12
the given range of values are: 13
the given range of values are: 14
the given range of values are: 15
the given range of values are: 16
the given range of values are: 17
the given range of values are: 18
the given range of values are: 19
the given range of values are: 20
the given range of values are: 21
the given range of values are: 22
    

#write a program to generate evens and odd up to given range          
print("even numbers:",end=" ")
for i in range(2,40,2):
    print(i,end=" ")
print ("odd numbera:",end=" ")
 
for x in range(1,40,2):
    print(x,end=" ")


output:
even numbers: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
odd numbera:1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 

#write a program to generate math table for a given number
n=int(input("enter the value:"))
for i in range(1,21):
    print(n," x ", i ," = ",n*i)

output:
enter the value:5
5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45
5  x  10  =  50
5  x  11  =  55
5  x  12  =  60
5  x  13  =  65
5  x  14  =  70
5  x  15  =  75
5  x  16  =  80
5  x  17  =  85
5  x  18  =  90
5  x  19  =  95
5  x  20  =  100


