# Pattern 5:Pyramid
'''
    *  
   **  
  ***  
 ****
 
'''
n=int(input("Enter the limit:"))
for i in range(1,n+1):  #run from 1 to n

    ''' First of all determining spaces and printing them.
    if the input is 3 then 2 spaces firstly as (n-i)---->(3-1)=2'''
    
    print(" "*(n-i),end=" ")
    print("*"*i,end=" ")
    print(" ")
    
    # for j in range(i):
    #     print("*",end=" ") 
    # print(" ") 
        

