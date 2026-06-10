#--------.leap year check,prime no. check and fibonacci series print

year=int(input("Enter the year:"))
if((year%4==0 and year%100!=0)or year%400==0):
    print("{} is a Leap Year".format(year))
else:
    print("{} is not a Leap Year".format(year))
n=int(input("Enter the no.:"))       
counter=0
for i in range(2,n):
    if(n%i==0):
        counter=counter+1
if(counter==0):
    print("{} is a Prime number".format(n))
else:
    print("{} is not a Prime number".format(n))
limit=int(input("Enter limit:"))    
a=0;b=1
print("Fibonacci series is give below:")
print(a,b,end=" ")
for i in range(2,limit+1):
    c=a+b
    print(c,end=" ")
    a=b;b=c