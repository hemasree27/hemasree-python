#find out numbers which are divisible with 3 and 9 in a given range
n=int(input("enter the value:"))
print("number divisible by 3 and 9:")
for x in range(1,n):
    if((x%3==0) and (x%9==0)):
        print(x,end=" ")
    


output:
enter the value:30
number divisible by 3 and 9:
9 18 27 


#implement a logic to find a given year is leap year or not
year=int(input("enter the year:"))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("given number is leap year")
        else:
            print("given number is not a leap year")
        
    else:
         print("given number is a leap year")
else:
    print("given number is not a leap year")



output:
enter the year:2024
given number is a leap year

enter the year:2032
given number is a leap year

enter the year:3000
given number is not a leap year


#print nunbers in a reverse order
n=int(input("enter the value:"))
for i in range(n,0,-1):
    print(i)

output:
enter the value:10
10
9
8
7
6
5
4
3
2
1
