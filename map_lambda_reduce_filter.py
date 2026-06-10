'''
Understanding map(),reduce(),filter(),lambda method
:-reduce() comes from module functools
'''

from functools import reduce
l1=["Saatvik ","Gupta"]
l=[12,14,23,21,46]
l2=[i if(i%2==0) else 0 for i in l] #list comprehension
print(l2)

#lambda method
# x=int(input("Enter a number to be squared:"))
x=5
square_lam=lambda x:x*x
print(square_lam(x))

#map function
def square(i):
    return i*i     #or simply square=lambda i:i*i
p=map(square,l2)   #map(function_name,iterable)
print(list(p))

#filter function
def check(j):
    if(j%2==0):
        return j*j
q=filter(check,l)
print(list(q))

#reduce function
def concat(a,b):
    return a+b
r=reduce(concat,l1)
print(str(r))