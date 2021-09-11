#1>Write a program to find the largest number in a line
num=[]
n=int(input("enter the numbers:")
for i in range(1,n+1):
    lis=int(input("enter element"))
    num.append(lis)
print("largest number in list:",max(num))
                                    

output:enter the numbers:5
enter element9
enter element0
enter element3
enter element76
enter element1
largest number in list: 76


#2>write a program to find the second largest number in a list
l=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
    b=int(input("Enter element:"))
    l.append(b)
l.sort()
print("Second largest element is:",l[num-2])

output
Enter number of elements:5
Enter element:7
Enter element:2
Enter element:8
Enter element:0
Enter element:9
Second largest element is: 8

#3>python Program to Put Even and Odd elements in a List into Two Different Lists

l=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
  lis=int(input("Enter element:"))
  l.append(lis)
even=[]
odd=[]
for j in l:
    if(j%2==0):
        even.append(j)
        
    else:
        odd.append(j)
        
even.sort()
odd.sort()
print("The even list",even)
print("The odd list",odd)

output:

Enter number of elements:6
Enter element:3
Enter element:4
Enter element:2
Enter element:1
Enter element:6
Enter element:7
The even list [2, 4, 6]
The odd list [1, 3, 7]



#4>write program to remove duplicate items from the list

num=[]
n=int(input("enter the numbers:"))
for i in range(1,n+1):
       lis=int(input("enter element"))
       num.append(lis)
print("largest number in list:",list(set(num)))


output
enter the numbers:7
enter element3
enter element3
enter element4
enter element5
enter element5
enter element6
enter element6
largest number in list: [3, 4, 5, 6]

#5>write a program to read a list of words and return the length of the longest one
l=[]
num=int(input("Enter number of elements:"))
for i in range(1,num+1):
  lis=str(input("Enter element:"))
  l.append(lis)
value=len(l[0])
large=l[0]
for x in l:
    if(len(x)>value):
        value=len(x)
        large=i
print("the largest word:",large)

output
Enter number of elements:4
Enter element:"hema"
Enter element:"vamsikrishna"
Enter element:"shobha"
Enter element:"swathi"
the largest word: "vamsikrishna"



#7>write a program to find are numbers in a range with perfect squares and sum of all digits in the number is less thnn 10

n=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]

while n<=u:
    for x in range(1,n):
        if x*x==n:
            print(n)
            
    n=n+1

output
Enter lower range: 1
Enter upper range: 20
4
9
16

        


