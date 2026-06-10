#----function for factorial of number using recursion

num=int(input("Enter the Number:"))

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)   #fruitful function as returns a value
store=factorial(num)
print("Factorial of {} is:".format(num),store)    

