# Pattern 2:Upper+Lower half pyramid

'''
*       ***        *
**   +  ** ------> **
***     *          ***  
                   **
                   *
'''

n=int(input("Enter the Limit:"))

# Making half pyramids---

for i in range(1,n+1):
    print("*"*i,end=" ")
    print(" ")

#here intialise j as n-1 as n already included in above loop
for j in range(n-1,0,-1):
    print("*"*j,end=" ")
    print(" ")    