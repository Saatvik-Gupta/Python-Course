#----------.List in python
"""1.List in python is mutable
2.Can be iterated forward and backword
3.can have heterogenous data items or elements
4.can have duplicate items."""
#list insertion and creation

l=[10,20,"Saatvik",2.22,11]
newl1=[]
newl2=list()    # both are list creation ways
newl1=l
newl2=l
#l.append(100) #to insert elements in list l as mutable changes
#l.append("Yo")
print(l)
newl1.insert(1,60)# to insert element at particular index
print(newl1)
newl2.extend([33,"Bye"]) # to insert like list only
print(newl2)
#Lets see deletion
l.pop(0)
newl1.remove(20)
print(l)
print(newl1)
print(newl2)