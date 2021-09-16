#find the evens in between range along with count and sum
n1=int(input("enter the start value:"))
n=int(input("enter a range:"))
def even(num):
    if num%2==0:
        return True
    return False

count=0
sum1=0
for i in range(n1,n+1):
    if even(i):
        print(i,end=" ")
        count+=1
        sum1+=i
print("even number between them",count)
print("sum of even number:",sum1)

output:
enter the start value:20
enter a range:50
20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 even number between them 16
sum of even number: 560

#find a given number is prime or not
n=int(input("enter the range:"))
def prime(num):
    for i in range(2,num):
        if(num%i)==0:
            return False
        return True
    #if it is prime it returns true otherwise false
print(prime(n))

output:
enter the range:7
True
enter the range:8
False


#print primes in a given range ,then print count
prim=int(input("enter a number:"))
def isprime(a):
        for i in range(2,a):
                if (a % i)==0:
                     return False
        return True
print("prime number is:")

count=0
for j in range(2,prim):
        if j>1:
                if isprime(j):
                        print(j,end=" ")
                        count+=1
print("count of prime numbers are:",count)


output:
enter a number:20
prime number is:
2 3 5 7 11 13 17 19 count of prime numbers are: 8


#print primes in between range then print count
num=int(input("enteer a number"))
prim=int(input("enter a number:"))

def isprime(a):
        for i in range(2,a):
                if (a % i)==0:
                        return False
        return True 

print("prime number is:")
count=0

for j in range(num,prim):
        if j>1:
                if isprime(j):
                        print(j,end=" ")
                        count+=1
print("count of prime numbers are:",count)

output:
nteer a number20
enter a number:50
prime number is:
23 29 31 37 41 43 47 count of prime numbers are: 7

#write a function to peint 5 multiples in a given rangeS
def mul():
        for i in range(1,n+1):
                if i%5==0:
                        print(i)
n=int(input("enter a range"))
mul()


output:
enter a range 40
5
10
15
20
25
30
35
40
       
 
