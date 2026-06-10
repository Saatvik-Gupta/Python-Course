#-----function to find max key in dictionary

d=dict()  #d={}

lim=int(input("Enter the limit of dictionary:"))
for i in range(lim):
    print("Enter {} index key and element:".format(i))
    k=int(input())
    value=input()
    d.update([(k,value)])  #or d[k]=value
print(d)   
val=d.keys() 
def maxkey(key):
    
    return max(key) # max() use in list as well as dictionary as well

store=maxkey(val)
print("Max value in dictionary {} is:".format(d),store)    

