# Pattern 1:Pyramid
'''
  *
 ***
*****
'''
n=int(input("Enter the limit:"))
for i in range(1,n+1):  #run from 1 to n

    ''' First of all determining spaces and printing them.
    if the input is 3 then 2 spaces firstly as (n-i)---->(3-1)=2'''
    
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")  # as odd number of stars use formula 2i-1
    print(" ")
