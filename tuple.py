#---------.Tuple data insertion
#Two methods---using "+" operator and converting tuple to list

#immutable to mutable conversion....

t=10,20,30,40 # or t=(10,20,30,40)

l=list(t) #converting tuple to list now all functions we use like append(),insert(),extend([])
l.insert(2,100)
print(l)
t=tuple(l)#converting list to tuple
print(t)
#2nd method using "+"
l1=(1,2,3,4)
l1=l1[0:1]+(5,)+l1[1:]
print(l1)
#same for deletion 1st convert to list use pop(),remove(),del l,clear()
