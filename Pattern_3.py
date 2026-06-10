# Pattern 3:Hollow and solid box
'''
Hollow Box--->  ****    Solid Box--->  ****
                *  *                   ****
                *  *                   ****
                ****                   ****
'''

n=int(input("Enter the Limit:"))

#Hollow box code
print("Printing Hollow Box--->")
for i in range(1,n+1):
    if(i==1 or i==n):   #First and last rows have complete stars
        print("*"*n,end=" ")
    else: #Middle section
        print("*",end="")
        print(" "*(n-2),end="") # for spaces in between
        print("*",end="")
    print(" ")       
     
#Solid box code
print("Printing Solid Box--->")
for j in range(1,n+1):
    print("*"*n,end=" ")
    print(" ")