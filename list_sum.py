#------Print sum of list elements

l=list()
s=0
lim=int(input("Enter the limit of list:"))
for i in range(lim):
    print("Enter {} index element:".format(i))
    val=int(input())
    l.append(val)
print(l)
for i in l:
    s=s+i
print("Sum of list elements:",s)   

#or simply use

print(sum(l))   


