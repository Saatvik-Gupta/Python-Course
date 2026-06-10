#---------.List comprehension

l=[20,30,55,65,2.2]
newl=[]
for i in l:
    if i%2==0:
        newl.append(i)
print(newl)   
newl2=[i for i in newl if i%4==0]   #  list comprehension multiple statements within shorter form
print(newl2)
print(l)

#-------------.list comprehension

l=["Rome","Chicago","India","Israil"]
for i in l:
    if(i.startswith("I")):
        l.remove(i) #when remove india index is at 2 then index move to 3 but israil occupied index 2 thats why israil not remove
    else:
        pass    
print(l)
newl=["Apple","Banana","Carrot","Chapati"]
newl=[i.upper() for i in newl if "a" in i] #agar keval if hai to for loop k baad
print(newl)
newl1=["Apple","Banana","Carrot"]
newl1=[i.upper() if "a" in i else "Hi" for i in newl1] #agar if-else dono then for loop se phele
print(newl1)
   