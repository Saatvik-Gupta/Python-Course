# Pattern 4:
'''
****
 ***
  **
   *
'''

n=int(input("Enter the Limit:"))
for i in range(n,0,-1):
    #marking spaces here firstly 0 spaces as i=n in first iteration
    print(" "*(n-i),end=" ") 
    print("*"*i,end=" ") #printing '*' iX times
    print(" ")
